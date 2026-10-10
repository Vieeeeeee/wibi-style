from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

import numpy as np
from PIL import Image, ImageColor, ImageDraw


ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ticket = load_script("ticket_finisher", "skills/personalized-print-ticket/scripts/finish_ticket.py")
triptych = load_script("triptych_compositor", "skills/underground-audition/scripts/compose_triptych_card.py")


class ImageFinishingTest(unittest.TestCase):
    def test_ticket_preserves_each_preset_ink_and_transparency(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "ticket.png"
            output = Path(directory) / "finished.png"
            for preset, config in ticket.PRESETS.items():
                with self.subTest(preset=preset):
                    Image.new("RGB", (2048, 769), config["paper"]).save(source)
                    ticket.finish(source, output, None, "#050505", 72, 36, preset)
                    with Image.open(output) as image:
                        self.assertEqual(image.mode, "RGBA")
                        self.assertEqual(image.getpixel((0, 0))[3], 0)
                        self.assertEqual(image.getpixel((image.width // 2, image.height // 2))[3], 255)
                        seam = round(image.width * ticket.PHOTO_SEAM_RATIO)
                        self.assertEqual(image.getpixel((seam, 86))[:3], ImageColor.getrgb(config["ink"]))

    def test_triptych_detects_white_warm_and_noisy_paper(self):
        for paper in ("#FFFFFF", "#F2F0E8", "#F7F5F0"):
            for noisy in (False, True):
                with self.subTest(paper=paper, noisy=noisy):
                    image = Image.new("RGB", (1024, 1024), paper)
                    if noisy:
                        noise = np.random.default_rng(7).integers(-3, 4, (1024, 1024, 1))
                        image = Image.fromarray(np.clip(np.array(image).astype(np.int16) + noise, 0, 255).astype(np.uint8))
                    draw = ImageDraw.Draw(image)
                    for x in (100, 380, 660):
                        draw.rectangle((x, 250, x + 240, 650), fill="#777777")
                    self.assertEqual(triptych.detect_band(image), (100, 250, 901, 651, [(241, 280), (521, 560)]))

    def test_triptych_rejects_missing_panel_or_empty_paper(self):
        image = Image.new("RGB", (1024, 1024), "#F2F0E8")
        with self.assertRaises(SystemExit):
            triptych.detect_band(image)
        draw = ImageDraw.Draw(image)
        for x in (100, 380):
            draw.rectangle((x, 250, x + 240, 650), fill="#777777")
        with self.assertRaises(SystemExit):
            triptych.detect_band(image)
