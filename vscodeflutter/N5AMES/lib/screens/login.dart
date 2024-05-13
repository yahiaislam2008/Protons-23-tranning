import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:n5ames/screens/HomePage.dart';
import 'package:n5ames/screens/regestrion.dart';
import 'package:n5ames/widgets/Infoscreen.dart';
class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState  extends State<LoginScreen> {

  TextEditingController _namecontroller = TextEditingController();
  var _namerror;
  // TextEditingController _emailcontrollaer = TextEditingController();
  // var _emailerorr;
  var _formKey = GlobalKey<FormState>();
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
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              " Hi Foodieee",
              style: TextStyle(
                fontSize: 35,
                fontWeight: FontWeight.w600,           
              ),
            ),
            Padding(
              padding: EdgeInsets.fromLTRB(20, 30, 20, 10),
              child: Form(
                key: _formKey,
                child: TextFormField(
                    validator: (value) {
                    if(value!.length <= 8) {
                      return"u have to put more than 8 letters";
                    }
                    return null; 
                    },
                    decoration: InputDecoration(
                      errorText: _namerror,
                      hintText: "Enter your Username or Email",
                      labelText: "Username or Email",
                      filled: true,
                      fillColor: Colors.white,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(20)),
                      )
                    ),
                    controller: _namecontroller ,
                  ),
              ),
            ),
                // Padding(
                //   padding: EdgeInsets.all(20),
                //   child: Form(
                //     child: TextFormField(
                //       validator: (value) {
                //           if (value!.length <= 18) {
                //             return"it's not real";
                //           }
                //           return null;
                //       },
                //       decoration: InputDecoration(
                //         errorText: _emailerorr,
                //         hintText: "Enter your Email@",
                //         labelText: "Eamil",
                //         filled: true,
                //         fillColor: Colors.white,
                //         border: OutlineInputBorder( 
                //           borderRadius: BorderRadius.all(Radius.circular(20)),
                //         )
                //       ),
                //       controller: _emailcontrollaer,
                //     ),
                //   ),
                // ),
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
                          print(_formKey.currentState);
                          print(_namecontroller);
                          print(_namerror);
                          // print(_emailcontrollaer);
                          // print(_emailerorr);
                          
                      setState(() {
                         if(_namecontroller.text.length <=8) {
                              _namerror = "u have to put more than 8 letters";
                            } 
                          // if(_emailcontrollaer.text.length <= 18) {
                          //     _emailerorr ="it's not real";
                          //   } 
                            // // if(_emailcontrollaer.text.length <= 30) {
                            // //   _emailerorr ="it's not real";
                            // } 
                            else {
                              // _emailcontrollaer;
                              _namecontroller;
                              // _emailerorr;
                              _namerror;
                              Navigator.of(context).push(
                                  MaterialPageRoute(
                                    fullscreenDialog: true,
                                    builder: (_) => HomePage()
                                    )
                               );
                             };
                          _namecontroller.clear();
                      
                       }); 
                        },   
                                
                        icon: Icon(
                          CupertinoIcons.chevron_right,
                          size: 15,
                          color: Colors.white,
                        ),
                         label: Text(
                          "N5AMES",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 12,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      )
                    ],
                  )
                ),
          ],
                ),
      ),
      );
      
  }
}