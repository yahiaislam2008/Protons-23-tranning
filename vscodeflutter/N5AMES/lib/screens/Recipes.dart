import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:n5ames/model/data.dart';
import 'package:n5ames/widgets/recipecard.dart';

class Recipes extends StatelessWidget {
  const Recipes({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
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
        ListView(
          padding: EdgeInsets.fromLTRB(20, 30, 20, 10),
          children: [
            Column(
              children: [
                TextField(
                  decoration: InputDecoration(
                    hintText: "Search...",
                    hintStyle: TextStyle(color: Colors.grey.shade600),
                    prefixIcon: Icon(
                      Icons.search,
                      color: Colors.grey.shade600,
                      size: 20,
                    ),
                    filled: true,
                    fillColor: Colors.grey.shade100,
             //       contentPadding: EdgeInsets.all(8),
                    border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(20)),
                        borderSide: BorderSide(color: Colors.grey.shade100)),
                  ),
                ),
                ...recipes.map((rec) => recipecard(recipe:rec)),
                // Padding(
                //   padding: EdgeInsets.fromLTRB(20, 30, 20, 10),
                //   child: Card(
                //     shape: RoundedRectangleBorder(
                //         borderRadius: BorderRadius.circular(15)),
                //     child: Padding(
                //       padding: const EdgeInsets.all(20),
                //       child: Column(
                //         children: [
                //           Text("ElMatba5".toUpperCase()),
                //           // Image(image: AssetImage("images/recipe.jpg"))
                //         ],
                //       ),
                //     ),
                //   ),
                // ),
              ],
            ),    
          ],
        ),
        Positioned(
            left: 0,
            right: 0,
            bottom: 0,
            child: Container(
              height: 80,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Theme.of(context)
                          .scaffoldBackgroundColor
                          .withOpacity(0.1),
                      Theme.of(context).scaffoldBackgroundColor,
                    ]),
              ),
            ),
          ),
      ]
      ),
    );
  }
}
