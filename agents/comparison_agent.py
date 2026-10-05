def compare_papers(paper1, paper2):

    comparison = f"""

Paper 1:
{paper1['title']}

Paper 2:
{paper2['title']}

Comparison:

Paper 1 Summary:
{paper1['abstract'][:200]}

Paper 2 Summary:
{paper2['abstract'][:200]}

Both papers belong to the same research area
but may use different methods and approaches.

"""

    return comparison