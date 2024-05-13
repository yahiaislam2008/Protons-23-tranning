import 'package:flutter/material.dart';
import 'package:n5ames/model/Message.dart';
import 'package:n5ames/model/data.dart';
import 'package:n5ames/model/friends.dart';
import 'package:n5ames/screens/Chats.dart';

class friendadd extends StatelessWidget {
  final Friend frien;
  const friendadd({super.key, required this.frien});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(elevation: 0,),
      body: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(20,5,15,550),
            child: Card(
              child: Padding(
                padding: const EdgeInsets.fromLTRB(15,30 ,15, 30),
                child: Column(
                  
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Text(
                      "Do u want to add this person",
                      style: TextStyle(
                        fontWeight: FontWeight.w200,
                        fontSize: 13,
                      ),
                    ),
                    SizedBox(
                      height: 5,
                    ),
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: [
                        Padding(
                          padding: const EdgeInsets.fromLTRB(30,15,15,0),
                          child: ElevatedButton(
                              onPressed: () {
                                Navigator.of(context).push(
                                    MaterialPageRoute(builder: (_) => Userscreen())
                                    );
                               //     friends.add(frien);
                                    messages.add(Message(name: frien.friendname, issentbyme: true));                                
                              },
                              child: Text("add ${frien.friendname}",style: TextStyle(fontSize: 10),)),
                        ),
                        Padding(
                          padding: const EdgeInsets.fromLTRB(30,15,15,0),
                          child: ElevatedButton(
                            onPressed: () {
                            Navigator.pop(context);
                          },
                           child: Text(
                            "cancel".toUpperCase(),
                            style: TextStyle(fontSize: 10)
                           )),
                        )
                      ],
                    )
                  ],
                ),
              ),
            ),
          ),
        
      ),
    );
  }
}
