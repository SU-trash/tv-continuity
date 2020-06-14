# tv-continuity
Quantitatively measuring continuity in TV shows (seriality and foreshadowing atm). Spoilers abound, obviously.

Currently focused on western animation shows due to personal interest but open to PRs for any type of show.
Still figuring out how far I'm going to run with this.

Also note that while I've done my best to apply a consistent system to all shows, the data is still quite subjective.

## Usage
`python3 show_continuity.py <module_name>`
will print summary statistics about the given show, including:
* Plot causality metrics:
    * Seriality %'s; overall and per-season
    * Branching factor (avg incoming causal connections of serial episodes); overall and per-season
* Foreshadowing metrics:
    * Avg instances of foreshadowing per episode
    * % eps with foreshadowing and % eps with 'major' foreshadowing
    * % foreshadowed eps and % eps with a 'major' element foreshadowed
    * Most foreshadowed ep
    
`python3 continuity_graph.py --serialities [<module 1> <module 2>]`
will create and open an HTML line chart (made with Plotly) comparing the seriality %'s of all
indicated shows, or all available shows if unspecified.

`python3 continuity_graph.py [--no-spoilers] <module_name>`
will create and open an HTML graph (made with Plotly) showing plot and foreshadowing connections
between episodes of the given show. If `--no-spoilers` is not included, nodes/edges will have
mouseover info giving details about each connection.

## Metrics
### Seriality
A measure of how serial (as opposed to episodic) a show is.
Currently calculated as (num_causal_eps + 1) / num_eps, where an episode is 'causal' if it causally 
affects the plot of any other episode. Connections with level Plot.REFERENTIAL aren't included.

This algorithm satisfies the following axioms I considered 'nice' (where each dot is an episode):
* `._.` = 1           (fully serial shows give score 1)
* `._. .` = 2/3       (scale intuitive)
* `. ._.` = `._. .`     (order-agnostic for isomorphic directed graphs)
* `.<:` = `._. .`     (episodes which cause many other episodes cannot have an undue effect on the score)
* `._._.` > `.<:`     (seriality worth more than plot-spawned episodic eps)
* `.<:>.` = `._._._.` (plot-spawned branches worth as much as serial if they converge again)
* `.<.>.` = `._._.`   (alternate paths between already-causally-connected episodes do not change the score)

I will also likely be updating this algorithm to something more complex to handle causal loops without
'over-inflating' the seriality % for episodes that include both plot progression and backstory.

### Foreshadowing
Separated into 'major' and 'minor'. Foreshadowing is considered 'minor' if it foreshadows the
mere existence of a place/person/object, rather than foreshadowing an event or revelation.
All other foreshadowing is currently considered 'major' regardless of any consideration to its
'importance'.
