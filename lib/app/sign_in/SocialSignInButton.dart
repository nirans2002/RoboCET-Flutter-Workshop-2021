import 'package:flutter/material.dart';
import 'package:time_tracker_app/components/custom_raised_widget.dart';

class SocialSignInButton extends CustomRaisedButton {
  SocialSignInButton({
    required String assetName,
    required text,
    required Color color,
    required Color textColor,
    required VoidCallback onPressed,
  }) : super(
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: <Widget>[
        Image.asset(assetName,),
        Text(
          text,
          style: TextStyle(color: textColor, fontSize: 15.0) ,
        ),
        Opacity(
          opacity: 0.0,
          child: Image.asset(assetName),
        ),
      ],
    ),
    color: color,
    onPressed: onPressed,
    borderRadius: 4.0,
  );
}
