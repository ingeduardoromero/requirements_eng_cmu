import argparse
from goalmodeling.schema import *


create_message_thread = Operation(
    name="Create Message Thread",
    category=OperationCategory.ENVIRONMENT_OPERATION
)
respond_to_thread = Operation(
    name="Respond to Thread",
    category=OperationCategory.ENVIRONMENT_OPERATION
)
react_to_message = Operation(
    name="React to Message",
    category=OperationCategory.ENVIRONMENT_OPERATION
)


agent_user_create_thread = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_respond_thread = Agent("User", AgentType.ENVIRONMENT_AGENT)
agent_user_react_message = Agent("User", AgentType.ENVIRONMENT_AGENT)


achieve_create_message_thread_if_convo_needs_org = AchieveGoal(
    name="CreateMessageThread <b>If</b> ConversationNeedsOrganization",
    performs=[PerformanceLink(agent_user_create_thread, create_message_thread)],
    refinements=None
)

achieve_respond_to_specific_thread = AchieveGoal(
    name="RespondToSpecificThread",
    performs=[PerformanceLink(agent_user_respond_thread, respond_to_thread)],
    refinements=None
)

achieve_react_to_message_for_acknowledgment = AchieveGoal(
    name="ReactToMessage <b>If</b> AcknowledgmentNeeded",
    performs=[PerformanceLink(agent_user_react_message, react_to_message)],
    refinements=None
)

purchase_additional_servers = Goal(
    goal_type=GoalType.BEHAVIORAL_GOAL,
    name="Increase number of servers"
)


limited_server_capacity = Obstacle(
    name="Limited Server Capacity",
     refinements=[Refinement(
        False,
        [purchase_additional_servers]
    )]
)

unable_to_handle_chat_velocity = Obstacle(
    "<b>Not able to handle chat load</b>",
    refinements=[
        Refinement(False, [limited_server_capacity]),
    ]
)

achieve_handle_async_quick_messages = AchieveGoal(
    name="HandleAsyncChatMessages",
    performs=None,
    refinements=[Refinement(
        complete=False,
        children=[
            achieve_create_message_thread_if_convo_needs_org,
            achieve_respond_to_specific_thread,
            achieve_react_to_message_for_acknowledgment,
            unable_to_handle_chat_velocity
        ]
    )]
)

server_resolution= ResolutionLink(purchase_additional_servers, limited_server_capacity)
async_obstruction = ObstructionLink(achieve_handle_async_quick_messages, unable_to_handle_chat_velocity)
