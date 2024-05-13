import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:n5ame/screens/HomePage.dart';
import 'package:n5ame/screens/regestrion.dart';
import 'package:n5ame/widgets/Infoscreen.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {

  TextEditingController _namecontroller = TextEditingController();
  var _namerror;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
      elevation: 0,
        leading: IconButton(
            onPressed: () {
              print("ok");
              Navigator.of(context).push(
                MaterialPageRoute(
                  fullscreenDialog: true,
                  builder: (_) => Infopage(),
                )
              );
            },
            icon: Icon(
              CupertinoIcons.info_circle,
              size: 24,
              color: Colors.black,
            )
            ),
            ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Padding(
            
            padding: EdgeInsets.fromLTRB(20, 30, 20, 10),
            child: TextField(
              
              decoration: InputDecoration(
                errorText: _namerror,
                hintText: "Enter your Username",
                labelText: "Username",
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.all(Radius.circular(20)),
                )
              ),
              controller: _namecontroller ,
            ),
          ),
          Padding(
            padding: EdgeInsets.all(20),
            child: TextField(
              decoration: InputDecoration(
                hintText: "Enter your Email@",
                labelText: "Eamil",
                filled: true,
                fillColor: Colors.white,
                border: OutlineInputBorder( //<----u ccan take as a value
                  borderRadius: BorderRadius.all(Radius.circular(20)),
                )
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(70, 0, 30, 0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                TextButton(
                  onPressed: () => Navigator.of(context).push(
                    MaterialPageRoute(
                      fullscreenDialog: true,
                      builder: (_) => Regestrionpage()
                    )
                  ),
                  child: Text(
                    "Regist",
                    style: TextStyle(
                      fontFamily: GoogleFonts.montserrat().fontFamily,
                      color: Colors.yellow
                    ),
                  ),
                ),
                SizedBox(
                  width: 50,
                ),
                ElevatedButton.icon(
                  onPressed: () {
                    setState(() {
                      if(_namecontroller.text.length <8)
                       _namerror = "u have to put more than 8 letters";
                      else;
                        Navigator.of(context).push(
                            MaterialPageRoute(
                              fullscreenDialog: true,
                              builder: (_) => HomePage()
                              )
                         );
                    });   
                  },
                  icon: Icon(
                    CupertinoIcons.chevron_right,
                    size: 15,
                    color: Colors.white,
                  )
                  , label: Text(
                    "5AMES",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 12,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                  
                ),
              ],
            ),
          )
        ],
      ),
    );
  }
}