from goalmodeling.schema import *
from goalmodeling.schema import ObstructionLink, Obstacle, AchieveGoal, Refinement


archive_one_email = Operation(
    name="Archive Single Email",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

archive_multiple_emails = Operation(
    name="Archive Multiple Emails",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

agent_user_single_archive = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_multiple_archive = Agent("User", AgentType.ENVIRONMENT_AGENT)


achieve_archived_single_email_if_one_selected = AchieveGoal(
    name="ArchivedSingleEmailIfOneSelected",
    performs=[PerformanceLink(agent_user_single_archive, archive_one_email)],
    refinements=None,
    leaf=True
)

achieve_archived_multiple_mails_if_multiple_selection = AchieveGoal(
    name="ArchivedMultipleMailsIfMultipleSelection",
    performs=[PerformanceLink(agent_user_multiple_archive, archive_multiple_emails)],
    refinements=None,
    leaf=True
)


mark_as_phishing = Operation(
    name="Mark Email as Phishing",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

move_to_spam_folder = Operation(
    name="Move Email to Spam Folder",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

quarantine_for_review = Operation(
    name="Move email to Quarantine For Review",
    category=OperationCategory.ENVIRONMENT_OPERATION
)

agent_user_mark_phishing = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_move_spam = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_quarantine = Agent("User", AgentType.ENVIRONMENT_AGENT)

not_g1 = Obstacle("<b>not</b> G1")
not_g2 = Obstacle("<b>not</b> G2")

not_achieve_mark_email_as_phishing=Obstacle("<b>Not Achieve Mark Email as Phising</b>", [Refinement(
            False,
            [not_g1]),
            Refinement(
            False,
            [not_g2])])

achieve_mark_email_as_phishing = AchieveGoal(
    name="MarkEmailAsPhishing",
    performs=[PerformanceLink(agent_user_mark_phishing, mark_as_phishing)],
    refinements=None,
    leaf=True
)


achieve_move_email_to_spam_folder = AchieveGoal(
    name="MoveEmailToSpamFolder",
    performs=[PerformanceLink(agent_user_move_spam, move_to_spam_folder)],
    refinements=None,
    leaf=True
)

#not_achieve_move_email_to_spam_folder = ObstructionLink(achieve_mark_email_as_phishing, not_achieve_mark_email_as_phishing)

not_achieve_move_email_to_spam_folder = ObstructionLink(
    goal= achieve_mark_email_as_phishing,
    obstacle= not_achieve_mark_email_as_phishing)


achieve_quarantine_email_for_review = AchieveGoal(
    name="QuarantineEmailForReview",
    performs=[PerformanceLink(agent_user_quarantine, quarantine_for_review)],
    refinements=None,
    leaf=True
)

achieve_handle_phishing_emails = AchieveGoal(
    name="HandlePhishingEmailsIfIdentified",
    performs=None,
    refinements=[
        Refinement(
            complete=True,
            children=[
                achieve_mark_email_as_phishing,
                not_achieve_mark_email_as_phishing
            ]
        ),
        Refinement(
            complete=True,
            children=[
                achieve_move_email_to_spam_folder,
            ]
        )
    ]
)

mark_email_as_read = Operation(
    name="Mark Email as Read",
    category=OperationCategory.ENVIRONMENT_OPERATION
)


agent_user_mark_read = Agent("User", AgentType.ENVIRONMENT_AGENT)


achieve_mark_email_as_read = AchieveGoal(
    name="MarkEmailAsRead",
    performs=[PerformanceLink(agent_user_mark_read, mark_email_as_read)],
    refinements=None,
    leaf=True
)

achieve_organize_emails = AchieveGoal(
    name="OrganizedEmailsIfNotAlready",
    performs=None,
    refinements=[Refinement(
        complete=False,
        children=[
            achieve_archived_single_email_if_one_selected,
            achieve_archived_multiple_mails_if_multiple_selection,
            achieve_handle_phishing_emails,
            achieve_mark_email_as_read  
        ],
        annotation="test annotation"  # Annotation not working.
    )]
)
