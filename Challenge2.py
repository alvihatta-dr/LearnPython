{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN8t8w+au/9LZoL9gSQl4WI",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/HattaAlvi/LearnPython/blob/main/Challenge2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cKjDuC48FFPX",
        "outputId": "bb585151-527c-494b-8a16-dc7db0ef4435"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your grade: 80\n",
            "Your grade is B\n",
            "Very Satisfy\n"
          ]
        }
      ],
      "source": [
        "grade = int(input(\"Enter your grade: \"))\n",
        "\n",
        "if (grade > 100) or (grade < 0):\n",
        "    print(\"Invalid value\")\n",
        "else:\n",
        "    if (grade <= 100) and (grade >= 90):\n",
        "        print(\"Your grade is A\")\n",
        "        print(\"With complement\")\n",
        "    elif (grade < 90) and (grade >= 80):\n",
        "        print(\"Your grade is B\")\n",
        "        print(\"Very Satisfy\")\n",
        "    elif (grade < 80) and (grade >= 70):\n",
        "        print(\"Your grade is C\")\n",
        "        print(\"Satisfying\")\n",
        "    elif (grade < 70) and (grade >= 60):\n",
        "        print(\"Your grade is D\")\n",
        "        print(\"Not Satisfactory\")\n",
        "    elif (grade < 59):\n",
        "        print(\"Your grade is E\")\n",
        "        print(\"Didn't PASS\")"
      ]
    }
  ]
}