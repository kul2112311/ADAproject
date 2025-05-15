# ADAproject
Project Title:
Tracking Paths in Polynomial Time – Implementation of Graph Algorithms

Overview
This project implements algorithms from the paper "Tracking Paths in Polynomial Time", which explores solutions to the Tracking Paths Problem—determining a minimal set of vertices (or edges) that uniquely track all s → t paths in a given graph. The problem is NP-hard in general, but the paper presents polynomial-time algorithms for chordal graphs, tournament graphs, and bounded-degree graphs.

# Project Structure
tests - to verify cases
implementation - python file with code
project proposal

# Setup & Requirements
Dependencies:

Python 3.x

NetworkX (for graph operations)

Matplotlib (for visualization)

# Tracking Paths in Polynomial Time - Project Documentation

## Problem Overview

The paper addresses the NP-hard problem of finding a minimal set of vertices to uniquely distinguish all simple paths between a source and destination in a graph. The problem is inherently difficult due to the complexity of graph structures. However, the paper's main contribution is the introduction of polynomial-time algorithms for certain graph types, namely chordal and tournament graphs, which are previously unexplored for path tracking problems.

The proposed algorithms are not only computationally efficient for these specific graph types but also offer practical applications in real-world systems such as network security (intrusion detection) and transportation logistics (route verification). The methods presented in the paper show how structural properties of graphs can enable efficient solutions to problems that are typically NP-hard.

## Key Contributions

- **Polynomial-Time Algorithms**: The paper introduces exact algorithms for chordal graphs and tournament graphs, solving the tracking problem more efficiently.
- **Edge-Based Tracking**: Unlike earlier approaches that were vertex-based, this paper shifts to edge-based tracking, which proves to be more efficient and allows for broader applications.
- **Approximation for Bounded-Degree Graphs**: The paper provides a 2(δ + 1)-approximation for graphs with degree δ ≥ 6, improving upon previous approximation results in the field.

## Algorithm Overview

### 1. **Chordal Graphs**
   - The algorithm leverages the chordal property (no induced cycles ≥ 4) by focusing on common neighbors in cycles. It identifies critical vertices that help distinguish all s-t paths.
   - The time complexity is O(m · n³), where m is the number of edges and n is the number of vertices.

### 2. **Tournament Graphs**
   - This algorithm focuses on identifying vertices in the out-neighborhood of a source vertex and the in-neighborhood of a destination vertex, ensuring that paths remain unique.
   - The time complexity is also O(m · n³), with preprocessing of O(n²).

## Complexity and Efficiency

- **Preprocessing**: Removing irrelevant vertices and edges runs in O(n²).
- **Main Algorithm**: The algorithm evaluates candidates for each edge, with a final complexity of O(m · n³).
- The paper demonstrates that these complexities are manageable for the specific graph classes, making the algorithms practical for use in real systems.

## Comparison with Previous Algorithms

Earlier work focused on planar graphs, with approximation algorithms for either shortest s-t paths or all s-t paths. While these approaches were limited to vertex-based solutions, this paper moves beyond these limitations by providing exact algorithms for broader graph classes like chordal and tournament graphs. Moreover, it shifts from vertex-based tracking to edge-based tracking, significantly improving efficiency and applicability.

## Hardness and Proofs

- **Vertex Cover Reduction**: The paper shows that the tracking problem is NP-hard by reducing it to the Vertex Cover problem, especially for graphs with degree δ ≥ 6.
- **Degree Constraint Analysis**: It proves that tracking remains NP-hard even when the maximum degree δ ≤ 6, though simpler cases might be tractable for δ ≤ 5.

## Implementation Challenges

Implementing the proposed algorithms presents several challenges:
- **Complex Graph Structures**: Managing large and complex chordal and tournament graphs can be computationally demanding.
- **Edge-Based Tracking**: Efficient computation of the minimum feedback edge set in large graphs adds complexity.
- **Handling Bounded-Degree Graphs**: For graphs with degree δ ≥ 6, the NP-hard nature of the problem requires approximation techniques to manage larger instances.

## Presentation Link (Youtube)

https://youtu.be/qqifYDh2a8c?si=sKHNu7CxKXCMM4LZ

## References Further 

[1] A. Banik, P. Choudhary, V. Raman, and S. Saurabh, Fixed-parameter tractable algorithms for tracking
shortest paths, arXiv preprint arXiv:2001.08977, 2020. Available at: http://arxiv.org/abs/2001.
08977
[2] D. Eppstein, M. T. Goodrich, J. A. Liu, and P. Matias, Tracking paths in planar graphs. In: Proceedings of the 30th International Symposium on Algorithms and Computation (ISAAC 2019), Shanghai
University of Finance and Economics, Shanghai, China, December 8–11, 2019, pp. 54:1–54:17.

