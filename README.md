***Repo***

*InitRepo*
    
    git init main
    git add .
    git commit -m 'some commits'

*CloneRepo*

    git clone someRepo


*Config*

    Set the user info for code submission
    
    git config --global user.name "yourname"
    git config --global user.email "youremail@gmail.com"



*GitHub*

    
    git remote add reponame ssh-url
    
    # Generate ssh key
    ssh-keygen -t rsa -C "youremail@example.com"
    cat ../.ssh/id_rsa.pub
  
    # Copy-paste the public key to Github SSH setting

    # setup the upstream fro push
    git push --set-upstream reponame master 

*Restore git *
     	You need to do two commands, the first will "unstage" the file (removes it from the list of files that are ready to be committed). Then, you undo the delete.

	If you read the output of the git status command (after the using git rm), it actually tells you how to undo the changes (do a git status after each step to see this).
	Unstage the file:

		git reset HEAD <filename>

	Restore it (undo the delete):

		git checkout -- <filename>



***Shell***

*Variable*

    Define: num=1 (no space is allowed)
    Apply: $num, num=2, num=$[ a+b ], let "num++"

    ${n} use the parameter in the script
    $* and $@ shows all the parameters
    $# # of parameters
    
*Array*

    Define: array=(A B "C" D)
    Apply: ${array[n]}, array[*/@], array[n]=2, 

    关联数组（hash map） declare -A site = ([key1]=value1 [key2]=value2)

    ${!site[*]} return all keys
    ${#site[*]} return # of pairs
        
*Operator*

    `expr 2 + 2`  vs  $[2+2]
    [ $a -? $b ]
    Comparsion: -eq -nq -gt -lt -ge -le
    bool: -o -a 
    logic: || &&
        echo " [ expr1 -o expr2 ] = [[ expr1 || expr2 ]]"
        echo " [ expr1 -a expr2 ] = [[ expr1 && expr2 ]]"
    character: -z -n = !=
    file: [ -? $file ]-r -w -x -d -f -s -e

*echo*

    echo -e
    echo -c
    echo ''  不进行转义
    echo `date`
    
*printf*

    printf "%2s %-5c %8d %4.2f"  "-" force to the left
    "" and '' are the same
     
*test*

    test arguments = [ arguments ]

*flow control*

    case
    1)
    ;;
    *)
    ;;
    esac

*function*

    functionname(){
        action
        [return ]
    }

    ${n} access inputs

    $? get the latest return value


***Docker in VScode ***

   	Install the extension
	Attach Docker to the Vscode


  
