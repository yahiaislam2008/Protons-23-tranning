import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:n5ames/model/modelrecipes.dart';

class foodrec extends StatelessWidget {
  final Recipe recip;
  const foodrec({
    super.key,
    required this.recip,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        leading: IconButton(
          onPressed: () =>
            Navigator.pop(context),
          icon: Icon(
            CupertinoIcons.back,
            size: 24,
            color: Colors.black,
          ),
        ),
      ),
      body: Stack(      
        children: [
          Padding(
            padding: EdgeInsets.fromLTRB(19,19,19,430),
            child: Card(
              child: Padding(
                padding: EdgeInsets.all(15),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Text(
                      "${recip.namerecipe}",
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    //Expanded(child: Image(image: AssetImage(recip.iamgeurl))),
                    Image(image: AssetImage(recip.iamgeurl),
                    height: 100,
                    width: 1000,),
                    Text(
                      "${recip.ingridents}",
                      style: TextStyle(
                        fontWeight: FontWeight.bold,
                      ),
                    )
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
