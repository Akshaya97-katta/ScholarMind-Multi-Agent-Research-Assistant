def generate_citation(paper):

    authors = ", ".join(paper["authors"])

    citation = (
        f"{authors} "
        f"({paper['published'][:4]}). "
        f"{paper['title']}."
    )

    return citation