import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:n5ames/screens/HomePage.dart';
import 'package:n5ames/screens/login.dart';
import 'package:n5ames/widgets/Infoscreen.dart';

class Regestrionpage extends StatefulWidget {
  const Regestrionpage({super.key});

  @override
  State<Regestrionpage> createState() => _RegestrionpageState();
}

class _RegestrionpageState extends State<Regestrionpage> {
  TextEditingController _emailcontrollaer = TextEditingController();
  var _emailerorr;
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
                Navigator.of(context).push(MaterialPageRoute(
                  fullscreenDialog: true,
                  builder: (_) => Infopage(),
                ));
              },
              icon: Icon(
                CupertinoIcons.info_circle,
                size: 24,
                color: Colors.black,
              )),
        ),
        body: Column(mainAxisAlignment: MainAxisAlignment.start, children: [
          Padding(
            padding: const EdgeInsets.all(20),
            child: Form(
              child: TextFormField(
                validator: (value) {
                  if (value!.length <= 8) {
                    return "u have to put more than 8 letters";
                  }
                  return null;
                },
                decoration: InputDecoration(
                    errorText: _namerror,
                    hintText: "Enter your Username",
                    labelText: "Username or Email",
                    filled: true,
                    fillColor: Colors.white,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(20)),
                    )),
                controller: _namecontroller,
              ),
            ),
          ),
          // ],

          Padding(
            padding: EdgeInsets.all(20),
            child: Form(
              child: TextFormField(
                validator: (value) {
                  if (value!.length <= 18) {
                    return "it's not real";
                  }
                  return null;
                },
                decoration: InputDecoration(
                    errorText: _emailerorr,
                    hintText: "Enter your Email@",
                    labelText: "Eamil",
                    filled: true,
                    fillColor: Colors.white,
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.all(Radius.circular(20)),
                    )),
                controller: _emailcontrollaer,
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.all(20),
            child: TextField(
              decoration: InputDecoration(
                  hintText: "Favorite food ❤❤",
                  labelText: "Favorite food",
                  filled: true,
                  fillColor: Colors.white,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.all(Radius.circular(20)),
                  )),
            ),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(70, 0, 30, 0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                TextButton(
                  onPressed: () => Navigator.of(context).push(MaterialPageRoute(
                      fullscreenDialog: true, builder: (_) => LoginScreen())),
                  child: Text(
                    "Log in",
                    style: TextStyle(
                        fontFamily: GoogleFonts.montserrat().fontFamily,
                        color: Colors.yellow),
                  ),
                ),
                SizedBox(
                  width: 50,
                ),
                ElevatedButton.icon(
                  onPressed: () { Navigator.of(context).push(MaterialPageRoute(
                      fullscreenDialog: true, builder: (_) => HomePage()));
                      _emailcontrollaer.clear();
                      },
                      
                  icon: Icon(
                    CupertinoIcons.chevron_right,
                    size: 15,
                    color: Colors.white,
                  ),
                  label: Text(
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
          ),
        ]));
  }
}
