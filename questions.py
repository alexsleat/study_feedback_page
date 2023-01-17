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
    
QUESTIONS = [
        ["PU1_VR", "radio_text", "Using the virtual reality interface enhances my correction of robot errors.", ["1", "2", "3", "4", "5"] ],
        ["PU2_VR", "radio_text", "Using the virtual reality interface enhances my productivity.",               ["1", "2", "3", "4", "5"] ],
        ["PU3_VR", "radio_text", "Using the virtual reality interface enhances my effectiveness.",              ["1", "2", "3", "4", "5"] ],
        ["PU4_VR", "radio_text", "I find the virtual reality interface useful.",                                ["1", "2", "3", "4", "5"] ],

        ["PU1_S", "radio_text", "Using the screen and keyboard interface enhances my correction of robot errors.",      ["1", "2", "3", "4", "5"]],
        ["PU2_S", "radio_text", "Using the screen and keyboard interface enhances my productivity.",                    ["1", "2", "3", "4", "5"]],
        ["PU3_S", "radio_text", "Using the screen and keyboard interface enhances my effectiveness.",                   ["1", "2", "3", "4", "5"]],
        ["PU4_S", "radio_text", "I find the screen and keyboard interface useful.",                                     ["1", "2", "3", "4", "5"]],

        ["PEOU1_VR", "radio_text", "Learning to use the virtual reality interface is easy for me.",                     ["1", "2", "3", "4", "5"]],
        ["PEOU2_VR", "radio_text", "My interaction with the virtual reality interface is clear and understandable.",    ["1", "2", "3", "4", "5"]],
        ["PEOU3_VR", "radio_text", "It would be easy for me to become skillful at using the virtual reality interface.", ["1", "2", "3", "4", "5"]],
        ["PEOU4_VR", "radio_text", "I find the virtual reality interface easy to use.",                                 ["1", "2", "3", "4", "5"]],

        ["PEOU1_S", "radio_text", "Learning to use the screen and keyboard interface is easy for me.",                          ["1", "2", "3", "4", "5"]],
        ["PEOU2_S", "radio_text", "My interaction with the screen and keyboard interface is clear and understandable.",         ["1", "2", "3", "4", "5"]],
        ["PEOU3_S", "radio_text", "It would be easy for me to become skillful at using the screen and keyboard interface.",     ["1", "2", "3", "4", "5"]],
        ["PEOU4_S", "radio_text", "I find the screen and keyboard interface easy to use.",                                      ["1", "2", "3", "4", "5"]],

        ["IU1_VR", "radio_text", "Assuming I have access to the virtual reality interface for correcting robot errors, I intend to use it.",                    ["1", "2", "3", "4", "5"]],
        ["IU2_VR", "radio_text", "Given that I have access to the virtual reality interface for correcting robot errors, I predict that I would use it.",       ["1", "2", "3", "4", "5"]],

        ["IU1_S", "radio_text", "Assuming I have access to the screen and keyboard interface for correcting robot errors, I intend to use it.",                 ["1", "2", "3", "4", "5"]],
        ["IU2_S", "radio_text", "Given that I have access to the screen and keyboard interface for correcting robot errors, I predict that I would use it.",    ["1", "2", "3", "4", "5"]],

        ["E1_VR", "radio_text", "Using the virtual reality interface is fun.",          ["1", "2", "3", "4", "5"]],
        ["E2_VR", "radio_text", "Using the virtual reality interface is exciting.",     ["1", "2", "3", "4", "5"]],
        ["E3_VR", "radio_text", "Using the virtual reality interface is enjoyable.",    ["1", "2", "3", "4", "5"]],
                
        ["E1_S", "radio_text", "Using the screen and keyboard interface is fun.",       ["1", "2", "3", "4", "5"]],
        ["E2_S", "radio_text", "Using the screen and keyboard interface is exciting.",  ["1", "2", "3", "4", "5"]],
        ["E3_S", "radio_text", "Using the screen and keyboard interface is enjoyable.", ["1", "2", "3", "4", "5"]],

        ["T1_VR", "radio_text", "The virtual reality interface is reliable.",           ["1", "2", "3", "4", "5"]],
        ["T2_VR", "radio_text", "The virtual reality interface is predictable.",        ["1", "2", "3", "4", "5"]],
        ["T3_VR", "radio_text", "The virtual reality interface is dependable.",         ["1", "2", "3", "4", "5"]],
        ["T4_VR", "radio_text", "The virtual reality interface is consistent.",         ["1", "2", "3", "4", "5"]],

        ["T1_S", "radio_text", "The screen and keyboard interface is reliable.",        ["1", "2", "3", "4", "5"]],
        ["T2_S", "radio_text", "The screen and keyboard interface is predictable.",     ["1", "2", "3", "4", "5"]],
        ["T3_S", "radio_text", "The screen and keyboard interface is dependable.",      ["1", "2", "3", "4", "5"]],
        ["T4_S", "radio_text", "The screen and keyboard interface is consistent.",      ["1", "2", "3", "4", "5"]]

]

RANZOMIZE_QUESTIONS = True