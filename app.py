from agents.paper_search import search_papers
from agents.summarizer import summarize_abstract
from agents.citation_agent import generate_citation
from agents.comparison_agent import compare_papers
from agents.research_gap_agent import find_research_gaps

topic = input("Enter research topic: ")

papers = search_papers(topic)

for i, paper in enumerate(papers, start=1):

    print("\n" + "=" * 80)

    print(f"\nPAPER {i}")

    print("\nTITLE:")
    print(paper["title"])

    print("\nAUTHORS:")
    print(", ".join(paper["authors"]))

    print("\nPUBLISHED:")
    print(paper["published"])

    print("\nLINK:")
    print(paper["link"])

    print("\nABSTRACT:")
    print(paper["abstract"])

    print("\nSUMMARY:")
    print(
        summarize_abstract(
            paper["abstract"]
        )
    )

    print("\nCITATION:")
    print(
        generate_citation(
            paper
        )
    )

# Comparison Agent

if len(papers) >= 2:

    print("\n" + "=" * 80)

    print("\nCOMPARISON REPORT")

    print(
        compare_papers(
            papers[0],
            papers[1]
        )
    )

# Research Gap Agent

print("\n" + "=" * 80)

print(
    find_research_gaps(
        papers
    )
)