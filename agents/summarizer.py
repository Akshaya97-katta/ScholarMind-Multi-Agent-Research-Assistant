def summarize_abstract(abstract):

    if len(abstract) > 300:
        return abstract[:300] + "..."

    return abstract