import 'package:flutter/material.dart';
import 'package:n5ames/model/modelrecipes.dart';
import 'foodrecipe.dart';

class recipecard extends StatelessWidget {
  final Recipe recipe;
  const recipecard({
    super.key,
    required this.recipe,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => Navigator.of(context).push(
        MaterialPageRoute(
            fullscreenDialog: true, builder: (_) => foodrec(recip: recipe)),
      ),
      child: Padding(
        padding: const EdgeInsets.only(top: 10),
        child: Card(
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
          child: Padding(
            padding: const EdgeInsets.all(30),
            child: Column(
              children: [
                Text(recipe.namerecipe.toUpperCase(),
                style: TextStyle(
                  fontSize: 30
                ),),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
