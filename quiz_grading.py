def main():
    #making a tuple witht the correct answers
    answerkey = ('A','C','A','B','B','D','D','A','C','A','B','C','D','C','B',)

    print("\nQuiz Grading App.....")
    #set process again constant to y so loop will work
    Process_Again = "y"
    #loop to prompt user for name and file and convert a file list to my own list.
    while Process_Again == "y":
        student_name = input("\nEnter the name of the student: ")
        file_name = input("Enter quiz answer file: ")

        try:
            #open the file to read into it
            fname = open(file_name, "r")

            #empty list to hold the student answers
            stuAnswerKey =[]

            #set line to first line of list
            line = fname.readline()

            while line != '':
                stuAnswerKey.append(line)
                line = fname.readline().rstrip("\n")

            fname.close
            
            print("student reponse from file")
            print(stuAnswerKey)
          #make an except so that if the file cannot be found it will give an error message  
        except FileNotFoundError:
            print("Error ... could not process"+ file_name)
            Process_Again = input("\nDo you have another student (y/n)?")
            
        #variables to use for loop to come
        index = 0
        correct_answers = 0
        incorrect_answers = 0
        
        #empty list for incorrect answers
        incorrect_answers_list = []
        #itterating thought the students asnwers to add onto correct or incorrect
        for answer in stuAnswerKey:
            if answer == answerkey[index]:
                correct_answers +=1
            else:
                incorrect_answers_list.append(index+1)
                incorrect_answers += 1
            index +=1
        #display the data retrieved and processed
        print("\n" + student_name + "'s Quiz results" + "\n"+ "-"*60 )
        print("Correct answers: "+ "\t"+ str(correct_answers))
        print("Incorrect answers: "+ "\t" + str(incorrect_answers),"(",incorrect_answers_list,")")
        #using an if else statement to display if student passed or failed
        if correct_answers >= 11:
            print("\nstudent PASSED the Quiz")
        else:
            print("\nStudent FAILED the Quiz")
        #prompting the user if there is another file
        Process_Again = input("\nDo you have another student (y/n)?")
        if Process_Again != "y":
            print("Goodbye!")

main()