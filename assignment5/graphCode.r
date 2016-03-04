#acquired from https://github.com/maturban/cs595-f13/tree/master/assignment9/latex
library(igraph)
g <- read.graph("karate.gml", format="gml")

print('Edges will be deleted in the following order : ')
## reading the graph	
repeat{
	edges_betweenness <- edge.betweenness(g)
	max_value <- max(edges_betweenness)
	edge_to_delete <- match(c(max_value),edges_betweenness)
	print(paste(paste(paste(get.edgelist(g)[edge_to_delete,1]," -> "),get.edgelist(g)[edge_to_delete,2]),paste("  -- Betweenness = ",max_value)))
	g <- delete.edges(g, E(g, P=c(get.edgelist(g)[edge_to_delete,1],get.edgelist(g)[edge_to_delete,2])))
	cluster_no <- clusters(g)['no']
	#making groups
	if(cluster_no == 2)

	{
		break
	} # coloring the graph
	cs <- leading.eigenvector.community(g, steps=1)
	V(g)$color <- ifelse(cs$membership==1, "green", "white")
	scale <- function(v, a, b) {
  	v <- v-min(v) ; v <- v/max(v) ; v <- v * (b-a) ; v+a
	}
	
	E(g)$color <- "grey"
	E(g)[ V(g)[ color=="green" ] %--% V(g)[ color=="white" ] ]$color <- "red"
	tkplot(g, layout=layout.kamada.kawai, vertex.label.font=2)
}
	##sorting the communities
cs <- leading.eigenvector.community(g, steps=1)
V(g)$color <- ifelse(cs$membership==1, "green", "white")
scale <- function(v, a, b) {
v <- v-min(v) ; v <- v/max(v) ; v <- v * (b-a) ; v+a
}
V(g)$size <- scale(abs(cs$eigenvectors[[1]]), 10, 20)
E(g)$color <- "grey"
E(g)[ V(g)[ color=="green" ] %--% V(g)[ color=="white" ] ]$color <- "red"
tkplot(g, layout=layout.kamada.kawai, vertex.label.font=2)

