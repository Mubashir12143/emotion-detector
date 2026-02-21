{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0ab5800-2a86-47ed-8e6d-88f0826a3478",
   "metadata": {},
   "outputs": [],
   "source": [
    "from EmotionDetection.emotion_detection import emotion_detector\n",
    "\n",
    "# Test with a sample input\n",
    "result = emotion_detector(\"I am so happy today!\")\n",
    "print(result)\n",
    "\n",
    "# Test empty input (should return error 400)\n",
    "result_empty = emotion_detector(\"\")\n",
    "print(result_empty)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a66fbf07-7077-47bd-904c-93dd25193020",
   "metadata": {},
   "outputs": [],
   "source": [
    ">>> from EmotionDetection.emotion_detection import emotion_detector\n",
    ">>> result = emotion_detector(\"I am so happy today!\")\n",
    ">>> print(result)\n",
    "{'text': 'I am so happy today!', 'anger': 0.01, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.04, 'dominant_emotion': 'joy', 'confidence': 0.95}\n",
    "\n",
    ">>> result_empty = emotion_detector(\"\")\n",
    ">>> print(result_empty)\n",
    "{'error': 'No input provided', 'status': 400}"
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
