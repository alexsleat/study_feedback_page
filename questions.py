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

    #Enjoyment
        ["E1_VR", "radio_text", "Using the virtual reality interface is fun.",          ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E2_VR", "radio_text", "Using the virtual reality interface is exciting.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E3_VR", "radio_text", "Using the virtual reality interface is enjoyable.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
                
        ["E1_S", "radio_text", "Using the screen and keyboard interface is fun.",       ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E2_S", "radio_text", "Using the screen and keyboard interface is exciting.",  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["E3_S", "radio_text", "Using the screen and keyboard interface is enjoyable.", ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],

    #Presence
        ["AA1_VR", "radio_text", "I was able to control events.",                                                       ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA2_VR", "radio_text", "The virtual environment was responsive to actions that I initiated (or performed).",                     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA3_VR", "radio_text", "I was able to anticipate what would happen next in response to the actions that I performed.",    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA4_VR", "radio_text", "I was able to actively survey or search the environment using vision.",              ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["AA1_S", "radio_text", "I was able to control events.",                                                        ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA2_S", "radio_text", "The virtual environment was responsive to actions that I initiated (or performed).",                      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA3_S", "radio_text", "I was able to anticipate what would happen next in response to the actions that I performed.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AA4_S", "radio_text", "I was able to actively survey or search the environment using vision.",               ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["AE1_VR", "radio_text", "I was able to examine objects closely.",                    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE2_VR", "radio_text", "I could examine objects from multiple viewpoints.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE3_VR", "radio_text", "I could concentrate on the assigned tasks or required activities rather than on the mechanisms used to perform those tasks or activities.",      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["AE1_S", "radio_text", "I was able to examine objects closely.",                    ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE2_S", "radio_text", "I could examine objects from multiple viewpoints.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["AE3_S", "radio_text", "I could concentrate on the assigned tasks or required activities rather than on the mechanisms used to perform those tasks or activities",      ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["IQ1_VR", "radio_text", "I experienced delays between my actions and expected outcomes.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ2_VR", "radio_text", "The visual display quality interfered or distracted me from performing assigned tasks or required activities.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ3_VR", "radio_text", "The control devices interfered with the performance of assigned tasks or with other activities.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
    
        ["IQ1_S", "radio_text", "I experienced delays between my actions and expected outcomes.",                                                ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ2_S", "radio_text", "The visual display quality interfered or distracted me from performing assigned tasks or required activities.",     ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
        ["IQ3_S", "radio_text", "The control devices interfered with the performance of assigned tasks or with other activities.",                  ["1", "2", "3", "4", "5"], ["Strongly Disagree", "Strongly Agree"] ],
]

QUESTION_ORDER = {

        "E1_": 1,
        "E2_": 2,
        "E3_": 3,
        "AA1_": 4,
        "AA2_": 5,
        "AA3_": 6,
        "AA4_": 7,
        "AE1_": 8,
        "AE2_": 9,
        "AE3_": 10,
        "IQ1_": 11,
        "IQ2_": 12,
        "IQ3_": 13

}