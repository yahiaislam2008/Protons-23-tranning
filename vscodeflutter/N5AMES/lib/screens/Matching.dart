import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:n5ames/model/data.dart';
import 'package:n5ames/model/modelrecipes.dart';
import 'package:n5ames/widgets/recipecard.dart';

class Matching extends StatefulWidget {
  const Matching({super.key});

  @override
  State<Matching> createState() => _MatchingState();
}
class _MatchingState extends State<Matching> {
  TextEditingController _match = TextEditingController();
  var _matcherror;
  var _formKey = GlobalKey<FormState>();
  var excite;
  var food;
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(
            CupertinoIcons.back,
            size: 24,
            color: Colors.black,
          ),
        ),
      ),
      body: Stack(
        alignment: Alignment.center,
        children: [
          SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                  padding: EdgeInsets.only(top: 16, left: 16, right: 16),
                  child: Form(
                    key: _formKey,
                    child: TextFormField(                    
                      validator: (value) {
                        if (value!.length < 3) {
                          return "u enter than 8 letters";
                        }
                        if (value.isEmpty) {
                          return "u didn't enter any thing";
                        }
                        for (var fo in recipes) {
                          if (fo == value) {
                            excite =true ;
                            food as Recipe;
                            food = fo;
                            print(fo.namerecipe);
                            return "i'm ok";
                          }
                        }                      
                       return null;
                      },
                      decoration: InputDecoration(
                        errorText: _matcherror,
                        hintMaxLines: 4,
                        helperMaxLines: 4,
                        errorMaxLines: 3,
                        hintText:
                            "Enter ingredients etween everyone enter a comma','",
                        hintStyle: TextStyle(color: Colors.grey),
                        // prefixIcon: Icon(
                        //   Icons.search,
                        //   color: Colors.grey,
                        //   size: 15,
                        // ),
                        filled: true,
                        fillColor: Colors.grey.shade600,
                        contentPadding: EdgeInsets.all(12),
                        border: OutlineInputBorder(
                            borderRadius: BorderRadius.all(Radius.circular(20)),
                            borderSide: BorderSide(color: Colors.grey)),
                      ),
                    controller: _match,
                    ),
                  ),
                ),
                Padding(
                  padding: EdgeInsets.fromLTRB(80, 10, 20, 0),
                  child: Row(
                    
                    crossAxisAlignment: CrossAxisAlignment.end,
                    children: [
                      ElevatedButton.icon(
                        onPressed: () {
                          print(_formKey.currentState);
                          print(_match);
                          print(_matcherror);
                          print(excite);
                          print(food);
                          for (var fo in recipes) {
                            if (fo.namerecipe == _match) {
                              fo = food as Recipe;
                              excite = true;
                            } 
                          }
                          setState(() {
                            if (_match.text.length < 3  && _match.text.isNotEmpty) {
                              _matcherror = "u enter less than 8 letters";
                            }
                            if (_match.text.isEmpty) {
                              _matcherror = "u didn't enter any thing";
                            }
                            
                            if (excite = true) {
                              print("fsalkj");
                              recipecard(recipe: food);
                              print(food.namerecipe);
                              // print("ok");
                              // excite =true ;
                              // food = e;
                             // recipecard(recipe: reci,);
                            }
                            // if (excite = true) {
                            //   recipecard(recipe: food);
                            // }                
                            else {
                              _matcherror = "not available now";
                            }
                          });                       
                        },
                        icon: Icon(
                          CupertinoIcons.search,
                          size: 15,
                        ),
                        label: Text(
                          "Match",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 12,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      )
                    ],
                  ),
                ),
                // if (excite == true)
                // recipecard(recipe: food),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
