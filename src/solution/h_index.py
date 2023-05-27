from typing import List


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        papers_count = len(citations)
        index = 0
        while index < papers_count and citations[papers_count - index - 1] >= index + 1:
            index += 1

        return index


    def hIndex1(self, citations: List[int]) -> int:
        papers_count = len(citations)
        # in this array we will keep the number of citations grouped by
        # e.g. if we have an array [0, 1, 9, 0] we will have the following citations_count_group:
        # [2, 1, 0, 0, 1], because there are 2 papers with 0 citations, 1 paper with 1 citation,
        # 0 paper with 2 citations, 0 paper with 3 citations and 1 paper with more than 3 citations
        # we keep citations_count + 1 elements and set as the last value the number of citations greater
        # than total number of citations, because even if we have citations: [10, 9, 4] the h index is 3
        citations_count_group = [0] * (papers_count + 1)
        for citation in citations:
            citations_count_group[min(citation, papers_count)] += 1

        print(f"{citations_count_group}")
        index = papers_count - 1
        while index >= 0:
            citations_count_group[index] += citations_count_group[index + 1]
            index -= 1

        print(f"{citations_count_group}")

        index = 0
        while index <= papers_count and citations_count_group[index] >= index:
            index += 1

        return index - 1

