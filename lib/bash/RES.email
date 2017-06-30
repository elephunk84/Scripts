#!/usr/bin/expect

set address "[lindex $argv 0]"
set subject "[lindex $argv 1]"
set ts_date "[lindex $argv 2]"
set ts_time "[lindex $argv 3]"

set timeout 10
spawn openssl s_client -connect smtp.gmail.com:465 -crlf -ign_eof 

expect "220" {
  send "EHLO localhost\n"

  expect "250" {
    send "AUTH PLAIN 3L3phunk84%\n"

    expect "235" {
      send "MAIL FROM: iaincstott@gmail.com\n"

      expect "250" {
        send "RCPT TO: <$address>\n"

        expect "250" {
          send "DATA\n"

          expect "354" {
            send "Subject: $subject\n\n"
            send "Email sent on $ts_date at $ts_time.\n"
            send "\n.\n"

            expect "250" {
                send "quit\n"
            }
          }
        }
      }
    }
  }
}
