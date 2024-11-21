import argparse
from goalmodeling.schema import *

not_g1 = Obstacle("<b>not</b> G1")
not_g2 = Obstacle("<b>not</b> G2")
not_g = Obstacle("<b>not</b> G", [
        Refinement(
        False,
        [not_g1]),
        Refinement(
        False,
        [not_g2])])

g1 = SoftGoal("G1")
g2 = SoftGoal("G2")
g = SoftGoal("G", None, [
        Refinement(False, [g1, g2])
    ])

g1_not_g1 = ObstructionLink(g1, not_g1)
g2_not_g2 = ObstructionLink(g2, not_g2)

output = generate_graph([g, not_g], [g1_not_g1, g2_not_g2])

print(output)
print(generate_pako_link(output))
print()