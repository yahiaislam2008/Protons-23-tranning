import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:n5ames/model/data.dart';
import 'package:n5ames/screens/Friends.dart';
import 'package:n5ames/widgets/chatscreen.dart';

class Userscreen extends StatefulWidget {
  const Userscreen({super.key});

  @override
  State<Userscreen> createState() => _UserscreenState();
}

class _UserscreenState extends State<Userscreen> {
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: (){
          Navigator.pop(context);
          },
          icon: Icon(
            CupertinoIcons.back,
              size: 24,
              color: Colors.black,
            ),
          ),
        actions: [
          IconButton(
            onPressed: () {
              Navigator.of(context).push(
                MaterialPageRoute(
                  builder: (_) => Friends()
                  )
              );
            },
             icon: Icon(
              CupertinoIcons.add,
              size: 24,
              color: Colors.black,
             )
            )
        ],
        ),
      body: Column(
        children: [
          ListView.builder(
            itemCount: messages.length,
            shrinkWrap: true,
            padding: EdgeInsets.only(top: 16),
            physics: NeverScrollableScrollPhysics(),
            itemBuilder: (context, index) {
              return chatscreen(
                name: messages[index].name,
                messageText: messages[index].text,
                isMessageRead: (index == 0 || index == 3) ? true : false, time: DateTime.now(),
              );
            },
          ),
        ],
      ), 
    );
  }
}
