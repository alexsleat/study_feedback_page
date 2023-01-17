# list of questions.
# ## Each questions is a list: 0: UID, 1: title, 2: response options
# QUESTIONS = {

#     1: [    ["Q01", "radio_text", "Multiple choice question", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q02", "radio_img", "Multiple choice with emoji tho (or pics)", ["1", "2","3", "4", "5"]],
#             ["Q03", "open_text", "Text response", [None]],
#     ],
#     2: [    ["Q11", "radio_text", "Did the robot move in an acceptable way?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q12", "radio_text", "Did the robot move as you would have expected?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q13", "radio_img", "Emoji Response", ["1", "2","3", "4", "5"]],
#             ["Q14", "radio_text", "Did the robot move in an acceptable way?", ["1", "2","3", "4", "5", "6", "7"]],
#             ["Q15", "radio_img", "What was the robot's task", ["artichoke", "basket","sandtimer"]]
#     ]
    
QUESTIONS = {
        "PU1_VR": "Using the virtual reality interface enhances my correction of robot errors.",
        "PU2_VR": "Using the virtual reality interface enhances my productivity.",
        "PU3_VR": "Using the virtual reality interface enhances my effectiveness.",
        "PU4_VR": "I find the virtual reality interface useful.",

        "PU1_S": "Using the screen and keyboard interface enhances my correction of robot errors.",
        "PU2_S": "Using the screen and keyboard interface enhances my productivity.",
        "PU3_S": "Using the screen and keyboard interface enhances my effectiveness.",
        "PU4_S": "I find the screen and keyboard interface useful.",

        "PEOU1_VR": "Learning to use the virtual reality interface is easy for me.",
        "PEOU2_VR": "My interaction with the virtual reality interface is clear and understandable.",
        "PEOU3_VR": "It would be easy for me to become skillful at using the virtual reality interface.",
        "PEOU4_VR": "I find the virtual reality interface easy to use.",

        "PEOU1_S": "Learning to use the screen and keyboard interface is easy for me.",
        "PEOU2_S": "My interaction with the screen and keyboard interface is clear and understandable.",
        "PEOU3_S": "It would be easy for me to become skillful at using the screen and keyboard interface.",
        "PEOU4_S": "I find the screen and keyboard interface easy to use.",

        "IU1_VR": "Assuming I have access to the virtual reality interface for correcting robot errors, I intend to use it.",
        "IU2_VR": "Given that I have access to the virtual reality interface for correcting robot errors, I predict that I would use it.",

        "IU1_S": "Assuming I have access to the screen and keyboard interface for correcting robot errors, I intend to use it.",
        "IU2_S": "Given that I have access to the screen and keyboard interface for correcting robot errors, I predict that I would use it.",

        "E1_VR": "Using the virtual reality interface is fun.",
        "E2_VR": "Using the virtual reality interface is exciting.",
        "E3_VR": "Using the virtual reality interface is enjoyable.",
                
        "E1_S": "Using the screen and keyboard interface is fun.",
        "E2_S": "Using the screen and keyboard interface is exciting.",
        "E3_S": "Using the screen and keyboard interface is enjoyable.",

        "T1_VR": "The virtual reality interface is reliable.",
        "T2_VR": "The virtual reality interface is predictable.",
        "T3_VR": "The virtual reality interface is dependable.",
        "T4_VR": "The virtual reality interface is consistent.",

        "T1_S": "The screen and keyboard interface is reliable.",
        "T2_S": "The screen and keyboard interface is predictable.",
        "T3_S": "The screen and keyboard interface is dependable.",
        "T4_S": "The screen and keyboard interface is consistent.",

}

RANZOMIZE_QUESTIONS = True