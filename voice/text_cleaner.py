import re


def clean_for_speech(text):

    if not text:
        return ""

    # Remove blocos de código
    text = re.sub(
        r"```.*?```",
        "",
        text,
        flags=re.DOTALL
    )

    # Remove código inline
    text = re.sub(
        r"`([^`]*)`",
        r"\1",
        text
    )

    # Remove negrito e itálico Markdown
    text = text.replace(
        "**",
        ""
    )

    text = text.replace(
        "__",
        ""
    )

    text = text.replace(
        "*",
        ""
    )

    text = text.replace(
        "_",
        ""
    )

    # Conversão de símbolos comuns
    text = text.replace(
        "US$",
        "dólares"
    )

    text = text.replace(
        "R$",
        "reais"
    )
    

    text = text.replace(
        "€",
        "euros"
    )

    text = text.replace(
        "£",
        "libras"
    )

    # Remove URLs
    text = re.sub(
        r"https?://\S+",
        "link",
        text
    )

    # Remove hashtags
    text = re.sub(
        r"#(\w+)",
        r"\1",
        text
    )

    # Remove excesso de espaços
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()