def read_template(file):# read template function with file path argument 
    with open(f"{file}")as f :#open the file 
        return f.read() # read the file and retrun the content of it 

def parse_template(txt): #parse_template function with text argument
     tuble=("Adjective","Adjective","Noun")# tuple
     text="It was a {} and {} {}."# text
     
     return text,tuble #return two values
 
def merge(txt,tuble): # merge function with text and tuble arguments
    result=txt.format(*tuble) #text with unpacking tuple format
    return result # retrun the merge text    

def story():
    print("**************************************************") # welcome message
    print("**          welcom to madlab game:)             ** ")
    print("**                                              ** ")
    print("**    madlab are a word replacement game        ** ")
    print("**\t\t")
    print("**    so you will enter some words and then     ** ")
    print("**\t\t")
    print("**    it will replace in a paragraph it         ** ")
    print("**\t\t")
    print("**   jsut answer the questions and press enter  ** ")
    print("**\t\t")
    print("**    to quit any time, type \"quit\"             ** ")# user should type quit to stop the game
    print("***************************************************" )     
    with open("./assets/story.txt")as file: # open story file 
        a=file.read()#read the file
    newList=[] # empty list that conten what user  add 
    #list with keywords for the game 
    list1=["Adjective","Adjective","A First Name","Past Tense Verb","A First Name","Adjective","Adjective","Plural Noun","Large Animal","Small Animal","A Girl's Name","Adjective","Plural Noun","Adjective","Plural Noun","Number 1-50","First Name","Number","Plural Noun","Number","Plural Noun"]
    for i in range(len(list1)): # looping in list1 
        
        g=input(list1[i]+">>") # take inputs user
        if g=="quit": # user should type quit to stop the game
           exit()# stop the game 
        if g=="": # validation
             print("please enter a value")
             g=input(list1[i]+">>")
        newList.append(g) # append to a newlsit
    
    result=a.format(*newList) # merge the file content with newlist in storing it inside result varible
    newfile=open("./assets/response.txt","x") # create a new file 
    newfile.write(result) #write result content inside the newf file
    newfile.close()# close the new file
    newfile=open("./assets/response.txt","r")#read the new file
    print("your game's descreption is as follows:")# result message 
    print(newfile.read())# print the result form the new file 
 



if __name__=="__main__":
    story()