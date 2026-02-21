{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0ab5800-2a86-47ed-8e6d-88f0826a3478",
   "metadata": {},
   "outputs": [],
   "source": [
    "# test_emotion_detection.py\n",
    "import unittest\n",
    "from EmotionDetection.emotion_detection import emotion_detector\n",
    "\n",
    "class TestEmotionDetector(unittest.TestCase):\n",
    "\n",
    "    def test_happy_text(self):\n",
    "        \"\"\"Test detection of joy.\"\"\"\n",
    "        text = \"I am so happy today!\"\n",
    "        result = emotion_detector(text)\n",
    "        self.assertIn('dominant_emotion', result)\n",
    "        self.assertEqual(result['dominant_emotion'], 'joy')\n",
    "        self.assertGreater(result['confidence'], 0.5)\n",
    "\n",
    "    def test_sad_text(self):\n",
    "        \"\"\"Test detection of sadness.\"\"\"\n",
    "        text = \"I feel very sad.\"\n",
    "        result = emotion_detector(text)\n",
    "        self.assertIn('dominant_emotion', result)\n",
    "        self.assertEqual(result['dominant_emotion'], 'sadness')\n",
    "        self.assertGreater(result['confidence'], 0.5)\n",
    "\n",
    "    def test_empty_text(self):\n",
    "        \"\"\"Test handling of empty input.\"\"\"\n",
    "        result = emotion_detector(\"\")\n",
    "        self.assertIn('error', result)\n",
    "        self.assertEqual(result['status'], 400)\n",
    "\n",
    "    def test_unknown_emotion(self):\n",
    "        \"\"\"Test neutral or ambiguous text.\"\"\"\n",
    "        text = \"I am walking to the store.\"\n",
    "        result = emotion_detector(text)\n",
    "        self.assertIn('dominant_emotion', result)\n",
    "        # Confidence might be low, but still returns a dominant_emotion key\n",
    "        self.assertIn(result['dominant_emotion'], ['joy','sadness','anger','fear','disgust'])\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    unittest.main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a66fbf07-7077-47bd-904c-93dd25193020",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24fff252-d7c3-4731-ae44-48bfd33c86b9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
