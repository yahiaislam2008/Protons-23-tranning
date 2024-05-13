import 'package:flutter/material.dart';
import 'package:grouped_list/grouped_list.dart';
import 'package:n5ames/model/Message.dart';
import 'package:chat_bubbles/chat_bubbles.dart';
import 'package:flutter/cupertino.dart';

class ChatPage extends StatefulWidget {
  const ChatPage({super.key});

  @override
  State<ChatPage> createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  List<Message> messages = [
    Message(
      text: "sure",
      issentbyme: true, name: 'mskadlkj',
    ),
    Message(
      text: "fsilahjj",
      issentbyme: false, name: 'ad;m;alsdm;lmsd',
    ),
    Message(
      text: "yahia is Ok",
      issentbyme: true, name: 'sak;sdla;ldk',
    ),
    Message(
      text: "3ayez 2nam",
      issentbyme: false, name: 'sdakdk;lkda;',

    ),
  ].reversed.toList();

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
        ),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: GroupedListView<Message, DateTime>(
                padding: const EdgeInsets.all(8),
                reverse: true,
                order: GroupedListOrder.DESC,
                useStickyGroupSeparators: true,
                floatingHeader: true,
                elements: messages,
                groupHeaderBuilder: (Message message) => SizedBox(
                  height: 40,
                  child: Center(
                    child: Card(
                      color: Theme.of(context).primaryColor,
                      child: Padding(
                        padding: EdgeInsets.all(8),
                        
                      ),
                    ),
                  ),
                ),
                itemBuilder: (context, Message message) => Align(
                  alignment: message.issentbyme
                  ? Alignment.centerRight
                  : Alignment.centerLeft,
                  child: BubbleSpecialThree(
                    text: message.text,
                    color: Color(0xFF1B97F3),
                    tail: false,
                    textStyle: TextStyle(color: Colors.white, fontSize: 16),
                // ), EdgeInsets.all(12),
                //                         child: Text(message.text),
                  ),
                ), groupBy: (message)  {DateTime(2008);
                return DateTime.now();}  , 
              ),
            ),
            //      ),
            //   ),
            
            MessageBar(

                  //  InputDecoration(
                  //   contentPadding: EdgeInsets.all(12),
                  //   hintText: "type your text....",
                  // ),
                  onSend: (text) {
                    final message = Message(
                      text: text,
                      issentbyme: true,
                    );
                    setState(() => messages.add(message));
                  },
                ),            
          ],
        ),
      ),
    );
  }
}


