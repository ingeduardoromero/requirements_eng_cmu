"""
Assignment 2 using the goal modeling library.
Author(s): Eddie Romero

"""

import argparse
from goalmodeling.schema import *
from subgoals.handleQuickMessages import *
from subgoals.searchEmail import *
from subgoals.organizeEmail import *
from subgoals.openedMailClient import *

def keepUpToDate_company_communication_using_email(host="https://mermaid.live"):

    achieve_keep_up_to_date_company_communication_inside_email = AchieveGoal(
        name="KeepUpToDateCompanyCommunicationUsingEmailClient",
        refinements=[
            Refinement(
                complete=False,
                children=[
                    achieve_opened_email_client,
                    achieve_organize_emails,
                    achieve_search_emails_using_nlp,
                    achieve_handle_async_quick_messages
                ]
            )
        ]
    )

    output = generate_graph([achieve_keep_up_to_date_company_communication_inside_email], [phishing_obstruction, phishing_resolution_label, phishing_resolution_ai, async_obstruction, server_resolution])
    link = generate_pako_link(output, mode="edit", host=host)

    print(output)
    print()
    print(link)
    # done

# def testing(host="https://mermaid.live"):
#     not_g1 = Obstacle("<b>not</b> G1")
#     not_g2 = Obstacle("<b>not</b> G2")
#     not_g = Obstacle("<b>not</b> G", [Refinement(
#             False,
#             [not_g1]),
#             Refinement(
#             False,
#             [not_g2])])

#     g1 = SoftGoal("G1")
#     g2 = SoftGoal("G2")
#     g = SoftGoal("G", None, [
#             Refinement(False, [g1, g2])
#         ])

#     g1_not_g1 = ObstructionLink(g1, not_g1)
#     g2_not_g2 = ObstructionLink(g2, not_g2)

#     output = generate_graph([g, not_g], [g1_not_g1, g2_not_g2])
#     link = generate_pako_link(output, mode="edit", host=host)

#     print(output)
#     print()
#     print(link)


def main():        
    keepUpToDate_company_communication_using_email()
    #testing()



if __name__ == "__main__":
    main()
