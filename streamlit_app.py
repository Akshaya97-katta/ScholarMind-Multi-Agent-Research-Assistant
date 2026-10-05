import streamlit as st

from agents.paper_search import search_papers
from agents.summarizer import summarize_abstract
from agents.citation_agent import generate_citation
from agents.comparison_agent import compare_papers
from agents.research_gap_agent import find_research_gaps

st.title("ScholarMind")

st.markdown("""
### AI Multi-Agent Research Assistant

Features:
- Paper Search Agent
- Summarization Agent
- Citation Agent
- Comparison Agent
- Research Gap Agent

Provides automated literature review and research-gap analysis.
""")

topic = st.text_input("Enter Research Topic")

if st.button("Search Papers"):

    papers = search_papers(topic)

    for i, paper in enumerate(papers, start=1):

        st.header(f"Paper {i}")

        st.write("### Title")
        st.write(paper["title"])

        st.write("### Authors")
        st.write(", ".join(paper["authors"]))

        st.write("### Published")
        st.write(paper["published"])

        st.write("### Link")
        st.write(paper["link"])

        st.write("### Abstract")
        st.write(paper["abstract"])

        st.write("### Summary")
        st.write(
            summarize_abstract(
                paper["abstract"]
            )
        )

        st.write("### Citation")
        st.write(
            generate_citation(
                paper
            )
        )

    if len(papers) >= 2:

        st.header("Comparison Report")

        st.write(
            compare_papers(
                papers[0],
                papers[1]
            )
        )

    st.header("Research Gap Analysis")

    st.write(
        find_research_gaps(
            papers
        )
    )