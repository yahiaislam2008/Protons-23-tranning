// import 'package:n5ames/model/Message.dart';
// import 'package:n5ames/model/Userchat.dart';

// List<ChatUsers> chatUsers = [
//     ChatUsers(name: "Jane Russel", messageText: "Awesome Setup", time: Message.)),
//     ChatUsers(name: "Glady's Murphy", messageText: "That's Great", time: DateTime.now().subtract(const Duration(days: 1,minutes: 23))),
//     ChatUsers(name: "Jorge Henry", messageText: "Hey where are you?", time: DateTime.now().subtract(const Duration(days: 3,minutes: 5))),
//     ChatUsers(name: "Philip Fox", messageText: "Busy! Call me in 20 mins", time: DateTime.now().subtract(const Duration(days: 5,minutes: 23))),
//     ChatUsers(name: "Debra Hawkins", messageText: "Thankyou, It's awesome", time: DateTime.now().subtract(const Duration(days: 6,minutes: 21))),
//     ChatUsers(name: "Jacob Pena", messageText: "will update you in evening", time: DateTime.now()),
//     ChatUsers(name: "Andrey Jones", messageText: "Can you please share the file?", time: DateTime.now().subtract(const Duration(minutes: 3))),
//     ChatUsers(name: "John Wick", messageText: "How are you?", time: DateTime.now().subtract(const Duration(days: 2,minutes: 3))),
//   ];


import 'package:flutter/cupertino.dart';
import 'package:n5ames/model/Message.dart';
import 'package:n5ames/model/friends.dart';
import 'package:n5ames/model/modelrecipes.dart';

List<Friend> friends = <Friend>[
  Friend(friendname: "yahia"),
  Friend(friendname: "yassen")
];
List<Message> messages = [
    Message(
      text: "sure",
      issentbyme: true,
      name: 'mskadlkj',
    ),
    Message(
      text: "fsilahjj",
      issentbyme: false,
      name: 'ad;m;alsdm;lmsd',
    ),
    Message(
      text: "yahia is Ok",
      issentbyme: true,
      name: 'sak;sdla;ldk',
    ),
    Message(
      text: "3ayez 2nam",
      issentbyme: false,
      name: 'sdakdk;lkda;',
    ),
  ].reversed.toList();
List<Recipe> recipes = <Recipe>[
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
    iamgeurl: "images/recipe.jpg"
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
    iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg"
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: Image(image: AssetImage("images/recipe.jpg")),
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  Recipe(
    namerecipe: "Pizza",
    ingridents: "tomatosause and <any topics u want> and some cheese",
  iamgeurl: "images/recipe.jpg",
  ),
  
];