import 'package:flutter/material.dart';

//contaner alaways have a child
// there is a thing that called safe area that can keeps u away from the status
//bar or the notsh for ios
//the benefit of the contanier (1.height ,2.widht) they control the size of the container,
//3.margin : that move the container away from the frame there is a
//func that keep every thing away from the containee
//and ther is also symmetric that make the top side = bottom side from veritacl and make left =right by horzantal
//and ther is to customise every side the func (fromLTBR)
//before all of this u have yo call somthing that called EdgeInsert
//4.we have padding that is the same funcs as margin moves the thing than in the container
// now we have column it ha ve childer that is containers u have vertacaldiricton and the is mainaxixalighment
//and there vis crossAxisAlignment note strech will let take the thing
//we can also make size between containers with no margin or padding
//to add icons foer row Icon then call it then see the icons
//ther is although the card widget
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: Scaffold(
            backgroundColor: Colors.red,
            body: SafeArea(
                child: Center(
                    child: Column(
              //    verticalDirection: VerticalDirection.down,
              //  mainAxisAlignment: MainAxisAlignment.end,
              //crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                // Container(
                //   width: 90,
                //   height: 60,
                //   // margin:EdgeInsets.all(30),
                //   // padding: EdgeInsets.fromLTRB(20, 10, 15, 5),
                //   color: Colors.blue,
                //   child: Text("i'm the best"),
                // ),
                // SizedBox(
                //   height: 20,
                //   width: 10,
                // ),
                // Container(
                //   width: 120,
                //   height: 50,
                //   //  margin:EdgeInsets.all(30),
                //   //padding: EdgeInsets.fromLTRB(20, 10, 15, 5),
                //   color: Colors.blue,
                //   child: Text("i'm the best"),
                // ),
                Container(
                  width: 90,
                  height: 50,
                  // margin:EdgeInsets.all(30),
                  // padding: EdgeInsets.fromLTRB(20, 10, 15, 5),
                  color: Colors.green,
                  child: Text("i'm the best"),
                ),
                Container(
                  width: 90,
                  height: 50,
                  // margin:EdgeInsets.all(30),
                  // padding: EdgeInsets.fromLTRB(20, 10, 15, 5),
                  color: Colors.yellow,
                  child: Text("i'm the best"),
                ),
                Card(
                    color: Colors.white,
                    margin: EdgeInsets.symmetric(horizontal: 80),
                    child: Padding(
                      padding: EdgeInsets.all(5),
                      //    padding: EdgeInsets.symmetric(vertical: 5,horizontal: 4),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.email_outlined,
                            color: Colors.blue,
                            size: 30,
                          ),
                          SizedBox(
                            width: 20,
                          ),
                          Text(
                            "email@gamil.com",
                            style: TextStyle(
                              color: Colors.amber,
                              fontSize: 17,
                              fontWeight: FontWeight.bold,
                            ),
                          )
                        ],
                      ),
                    )),
                    const Card(
                      margin: EdgeInsets.symmetric(horizontal: 80),
                      color: Colors.blue,
                      child: ListTile(
                        leading: Icon(
                          Icons.more_vert_rounded,
                          size: 20,
                          color: Colors.black,
                        ),
                      
                        title: Text(
                          "sure",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 18,
                            fontWeight:FontWeight.bold,
                          ),
                        ),
                        trailing: Icon(
                          Icons.more_vert_rounded,
                          size: 20,
                          color: Colors.black,
                        )
                      ),  
                    )
              ],
            )))));
  }
}
