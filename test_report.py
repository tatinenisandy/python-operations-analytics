import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from report import calculate_metrics

class TestReport(unittest.TestCase):
    def test_sample_metrics(self):
        result = calculate_metrics()
        self.assertEqual(result["total_tickets"], 6)
        self.assertEqual(result["resolution_rate_pct"], 66.7)
        self.assertEqual(result["avg_resolution_hours"], 11.8)

if __name__ == "__main__":
    unittest.main()
