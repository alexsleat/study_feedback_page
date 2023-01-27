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
    #Perceived Usability
        ["PU1_VR", "radio_text", "Using the virtual reality interface enhances my correction of robot errors.", ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PU2_VR", "radio_text", "Using the virtual reality interface enhances my productivity.",               ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"]  ],
        ["PU3_VR", "radio_text", "Using the virtual reality interface enhances my effectiveness.",              ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"]  ],
        ["PU4_VR", "radio_text", "I find the virtual reality interface useful.",                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"]  ],

        ["PU1_S", "radio_text", "Using the screen and keyboard interface enhances my correction of robot errors.",      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PU2_S", "radio_text", "Using the screen and keyboard interface enhances my productivity.",                    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PU3_S", "radio_text", "Using the screen and keyboard interface enhances my effectiveness.",                   ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PU4_S", "radio_text", "I find the screen and keyboard interface useful.",                                     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

    #Perceived Ease of Use
        ["PEOU1_VR", "radio_text", "Learning to use the virtual reality interface is easy for me.",                     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU2_VR", "radio_text", "My interaction with the virtual reality interface is clear and understandable.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU3_VR", "radio_text", "It would be easy for me to become skillful at using the virtual reality interface.", ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU4_VR", "radio_text", "I find the virtual reality interface easy to use.",                                 ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU5_VR", "radio_text", "It is easy to match the virtual world with the real world using the virtual reality interface.", ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

        ["PEOU1_S", "radio_text", "Learning to use the screen and keyboard interface is easy for me.",                          ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU2_S", "radio_text", "My interaction with the screen and keyboard interface is clear and understandable.",         ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU3_S", "radio_text", "It would be easy for me to become skillful at using the screen and keyboard interface.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU4_S", "radio_text", "I find the screen and keyboard interface easy to use.",                                      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["PEOU5_S", "radio_text", "It is easy to match the virtual world with the real world using the screen interface.",      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

    #Intention to Use
        ["IU1_VR", "radio_text", "Assuming I have access to the virtual reality interface for correcting robot errors, I intend to use it.",                    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IU2_VR", "radio_text", "Given that I have access to the virtual reality interface for correcting robot errors, I predict that I would use it.",       ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

        ["IU1_S", "radio_text", "Assuming I have access to the screen and keyboard interface for correcting robot errors, I intend to use it.",                 ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IU2_S", "radio_text", "Given that I have access to the screen and keyboard interface for correcting robot errors, I predict that I would use it.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

    #Enjoyment
        ["E1_VR", "radio_text", "Using the virtual reality interface is fun.",          ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E2_VR", "radio_text", "Using the virtual reality interface is exciting.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E3_VR", "radio_text", "Using the virtual reality interface is enjoyable.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
                
        ["E1_S", "radio_text", "Using the screen and keyboard interface is fun.",       ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E2_S", "radio_text", "Using the screen and keyboard interface is exciting.",  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E3_S", "radio_text", "Using the screen and keyboard interface is enjoyable.", ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

    #Presence
        ["AA1_VR", "radio_text", "I was able to control the events.",                                                       ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA2_VR", "radio_text", "The environment was responsive to actions that I initiated (or performed).",                     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA3_VR", "radio_text", "I was able to anticipate what would happen next in response to the actions that I performed.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA4_VR", "radio_text", "I was able to actively survey or search the environment using vision.",              ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["AA1_S", "radio_text", "I was able to control the events?",                                                        ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA2_S", "radio_text", "The environment was responsive to actions that I initiated (or performed).",                      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA3_S", "radio_text", "I was able to anticipate what would happen next in response to the actions that I performed.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA4_S", "radio_text", "I was able to actively survey or search the environment using vision.",               ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["AE1_VR", "radio_text", "I was able to examine objects closely.",                    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE2_VR", "radio_text", "I could examine objects from multiple viewpoints",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE3_VR", "radio_text", "I could concentrate on the assigned tasks or required activities rather than on the mechanisms used to perform those tasks or activities?",      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["AE1_S", "radio_text", "I was able to examine objects closely.",                    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE2_S", "radio_text", "I could examine objects from multiple viewpoints",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE3_S", "radio_text", "I could concentrate on the assigned tasks or required activities rather than on the mechanisms used to perform those tasks or activities",      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["IQ1_VR", "radio_text", "I experienced a delay between my actions and expected outcomes.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ2_VR", "radio_text", "The visual display quality interfered or distracted me from performing assigned tasks or required activities.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ3_VR", "radio_text", "The control devices interfered with the performance of assigned tasks or with other activities.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["IQ1_S", "radio_text", "I experienced a delay between my actions and expected outcomes.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ2_S", "radio_text", "The visual display quality interfered or distracted me from performing assigned tasks or required activities.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ3_S", "radio_text", "The control devices interfered with the performance of assigned tasks or with other activities.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

    #NASA TLX
    
        ["NASA1_VR", "radio_text", "The task was mentally fatiguing.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA2_VR", "radio_text", "The task was phyiscally fatiguing.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA3_VR", "radio_text", "I felt hurried or rushed during the task.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA4_VR", "radio_text", "I felt insecure, discouraged, irritated, stressed or annoyed.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA5_VR", "radio_text", "The task was complex.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA6_VR", "radio_text", "I felt stressed whilst performing the task.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA7_VR", "radio_text", "The task environment was distracting.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA8_VR", "radio_text", "The visual and auditory aspects of the task were were uncomfortable/irritating.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA9_VR", "radio_text", "The task was difficult to control/navigate.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],


        ["NASA1_S", "radio_text", "The task was mentally fatiguing.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA2_S", "radio_text", "The task was phyiscally fatiguing.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA3_S", "radio_text", "I felt hurried or rushed during the task.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA4_S", "radio_text", "I felt insecure, discouraged, irritated, stressed or annoyed.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA5_S", "radio_text", "The task was complex.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA6_S", "radio_text", "I felt stressed whilst performing the task.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA7_S", "radio_text", "The task environment was distracting.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA8_S", "radio_text", "The visual and auditory aspects of the task were were uncomfortable/irritating.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["NASA9_S", "radio_text", "The task was difficult to control/navigate.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
]

RANZOMIZE_QUESTIONS = True
