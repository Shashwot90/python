# not evaluated first then and then or
#False or not True and True ==> not true i.e. false. false or false and true ; false or false == false

#False and not True or True ===>false and false or true => false or true => true

#True and not (False or False) ==> true and not false => true and true => true

#not not True or False and not True ==> not false or false and false => true or false and false => true or false => true

#False or not (True and True) ==> false or not true => false false => false
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)