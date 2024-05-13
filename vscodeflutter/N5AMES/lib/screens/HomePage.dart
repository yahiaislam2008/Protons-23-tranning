import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:n5ames/screens/Chats.dart';
import 'package:n5ames/screens/Matching.dart';
import 'package:n5ames/screens/Recipes.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
    //  backgroundColor: Colors.white,
      
      appBar: AppBar(
          elevation: 0,
          centerTitle: true,
          title: Text("N5MES",
          style: TextStyle(
            fontStyle: GoogleFonts.aboreto().fontStyle,
            color: Colors.black,
          ),)          
        ),
        body:
         Stack(
        alignment: Alignment.center,
        children: [
          SafeArea(
            child: ListView(
              children: [
                GestureDetector(
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                          fullscreenDialog: true, builder: (_) => Matching()),
                    );
                  },
                  child: Padding(
                    padding: EdgeInsets.fromLTRB(20, 30, 20, 10),
                    child: Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15)),
                      child: Padding(
                        padding: const EdgeInsets.all(20),
                        child: Column(
                          children: [
                            Text("Matching Food 🍔🍕🍖".toUpperCase()),
                            Image(image: AssetImage("images/recipe.jpg"))
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                          fullscreenDialog: true, builder: (_) => Recipes()),
                    );
                  },
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(20, 30, 20, 10),
                    child: Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15)),
                      child: Padding(
                        padding: const EdgeInsets.all(20),
                        child: Column(
                          children: [
                            Text("Zabat W Kalamny ✌✌".toUpperCase()),
                            Image(image: AssetImage("images/recipe.jpg"))
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                          fullscreenDialog: true, builder: (_) => Userscreen()),
                    );
                  },
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(20, 30, 20, 10),
                    child: Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15)),
                      child: Padding(
                        padding: const EdgeInsets.all(20),
                        child: Column(
                          children: [
                            Text("Chat 📣👋🙌".toUpperCase()),
                            Image(image: AssetImage("images/recipe.jpg"))
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
                ListTile(
                  title: Text("d;kljlkgdf"),
                 // isThreeLine: true,
          //        subtitle: Text("sdgdfd"),
                ),
                GestureDetector(
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                          fullscreenDialog: true, builder: (_) => Recipes()),
                    );
                  },
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(20, 30, 20, 10),
                    child: Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15)),
                      child: Padding(
                        padding: const EdgeInsets.all(20),
                        child: Column(
                          children: [
                            Text("recipes 🧾🧾".toUpperCase()),
                            Image(image: AssetImage("images/recipe.jpg"))
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
                GestureDetector(
                  onTap: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                          fullscreenDialog: true, builder: (_) => Recipes()),
                    );
                  },
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(20, 30, 20, 10),
                    child: Card(
                      shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(15)),
                      child: Padding(
                        padding: const EdgeInsets.all(20),
                        child: Column(
                          children: [
                            Text("meal packs 🍴🍴".toUpperCase()),
                            Image(image: AssetImage("images/recipe.jpg"))
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
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
        ],
      ),
    );
  }
}
