import 'package:flutter/material.dart';
import 'package:n5ames/screens/Chatpage.dart';

class chatscreen extends StatefulWidget {
  // const chatscreen({super.key});
  String name;
  String messageText;
  DateTime time;
  bool isMessageRead;
  chatscreen({
    super.key,
    required this.name,
    required this.messageText,
    required this.time,
    required this.isMessageRead,
  });

  @override
  State<chatscreen> createState() => _chatscreenState();
}

class _chatscreenState extends State<chatscreen> {
  // List<Message> messages = [
  //   Message(
  //     text: "sure",
  //     date: DateTime.now().subtract(Duration(days: 3, minutes: 3)),
  //     issentbyme: true,
  //     isnassegeread: true
  //   ),
  //   Message(
  //     text: "fsilahjj",
  //     date: DateTime.now().subtract(Duration(days: 3, minutes: 4)),
  //     issentbyme: false,
  //   ),
  //   Message(
  //     text: "yahia is Ok",
  //     date: DateTime.now().subtract(Duration(days: 3, minutes: 5)),
  //     issentbyme: true,
  //     isnassegeread: true,
  //   ),
  //   Message(
  //     text: "3ayez 2nam",
  //     date: DateTime.now().subtract(Duration(minutes: 1)),
  //     issentbyme: false,
  //     isnassegeread: false,
  //   ),
  // ].reversed.toList();

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        Navigator.of(context).push(
          MaterialPageRoute(fullscreenDialog: true, builder: (_) => ChatPage()),
        );
      },
      child: Container(
        padding: EdgeInsets.only(left: 16, right: 16, top: 10, bottom: 10),
        child: Row(
          children: <Widget>[
            Expanded(
              child: Row(
                children: <Widget>[
                  CircleAvatar(
                    backgroundColor: Colors.orange,
                    maxRadius: 30,
                  ),
                  SizedBox(
                    width: 16,
                  ),
                  Expanded(
                    child: Container(
                      color: Colors.transparent,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Text(
                            widget.name,
                            style: TextStyle(fontSize: 16),
                          ),
                          SizedBox(
                            height: 6,
                          ),
                          Text(
                            widget.messageText,
                            style: TextStyle(
                                fontSize: 13,
                                color: Colors.grey.shade600,
                                fontWeight: widget.isMessageRead
                                    ? FontWeight.bold
                                    : FontWeight.normal),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
            // Text(
            //   DateTime.parse(widget.time as String) as String,
            //   style: TextStyle(
            //       fontSize: 12,
            //       fontWeight: widget.isMessageRead
            //           ? FontWeight.bold
            //           : FontWeight.normal),
            // ),
          ],
        ),
      ),
    );
  }
}