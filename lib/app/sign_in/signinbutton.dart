import 'package:flutter/material.dart';
import 'package:time_tracker_app/components/custom_raised_widget.dart';

class SignInButton extends CustomRaisedButton {
  SignInButton({
    required String text,
    required Color color,
    required Color textColor,
    required VoidCallback onPressed,
    required borderRadius,
  }) : super(
          child: Text(
            text,
            style: TextStyle(color: textColor, fontSize: 15.0),
          ),
          color: color,
          onPressed: onPressed,
          borderRadius: borderRadius,
        );
}
