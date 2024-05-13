class Message {
   
  String text ;
  final bool issentbyme;
  bool isnassegeread;
  var name;
  Message({
    this.text = " ",
    required this.issentbyme,
    this.isnassegeread =false,
    this.name =null,
  });
}
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
