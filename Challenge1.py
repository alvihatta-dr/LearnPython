{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOdV1sN0jU+L/eTWPceMUiX",
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
        "<a href=\"https://colab.research.google.com/github/HattaAlvi/LearnPython/blob/main/Challenge1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cKjDuC48FFPX",
        "outputId": "df17921e-d8f6-42b6-a206-3caba5c5db73"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your password: ··········\n",
            "Welcome alvihatta to the dashboard of the Program\n"
          ]
        }
      ],
      "source": [
        "\n",
        "from getpass import getpass\n",
        "\n",
        "username = \"alvihatta\"\n",
        "password = \"administrator\"\n",
        "\n",
        "user_password = getpass(\"Enter your password: \")\n",
        "if user_password == password:\n",
        "    print(f\"Welcome {username} to the dashboard of the Program\")\n",
        "else:\n",
        "    print(\"Your credentials are wrong. Please try again.\")"
      ]
    }
  ]
}