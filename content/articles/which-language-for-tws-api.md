Title: Which language to use with TWS API (Interactive Brokers API)?
Date: 2017-03-26 21:23
Category: finance
Tags: investing, api, interactive brokers, tws
Authors: Rok Povšič

# TWS API

Interactive Brokers has an API called [TWS API](https://interactivebrokers.github.io) which you can use to programmatically
execute trades, poll current/historical market data, get account info, open positions, etc.
Official bindings for several programming languages exist, namely: C#, Java, C++, VB, and Python.

All the TWS API functionality is supported in all of those programming languages. Which language should you choose for your
trading program?

### C#
C# is a programming language made by Microsoft, although you can run it on Linux too. It's a statically-typed, which means all variable types
are known at the compile time. That means your IDE, in this case probably Visual Studio, knows all the variable types and can help you
a lot when writing code.

Since C# is primarily a language that runs on Windows, you'll most likely want to use it on that platform.
These days when .NET is becoming more platform-independent, it could maybe be used on Linux/Max also although I haven't tried it yet.
Most likely I'd just use Java on those platforms.

### Java
Java is similar to C# (it's more proper to say it the other way around since C# was created after and was greatly inspired by Java)
although it's more bare-boned. You could argue there's less
batteries included although that'd probably depend on the developer.

You can run trading programs written in Java on Linux, Windows, and Mac.

### C++
C++ is the oldest programming language here, and the most low-level. Its advantages are speed and the increased control.

There several reasons why I don't recommend using C++ for the use with TWS API. The first is that the development speed is much slower.
With increased control comes increased needed time investment to do an equivalent trading program in C++ compared to other
TWS-supported programming languages on the list.

But what if speed is really important to you and you are prepared to invest more time and resources to be fast? In that case choosing
Interactive Brokers might not be the best option. Its servers are probably located somewhere far away from where your server is
located, and the time needed for the data to travel over the network is probably much larger than that of running the trading program.

I'd only use C++ in the case where a heavy algorithm needs to be run in real-time, calculating, for example, some large matrixes.
Although even in that case it'd probably be better to use single-threaded Java with Garbage Collector disabled, or something like that.

### VB
You don't want to use VB. Its variants take 3 out of 4 places for the most dreaded languages in the [Stack Overflow's 2017 Developer Survey](https://stackoverflow.com/insights/survey/2017). Use it only if its the only language you know.

### Python
Although still only supported by the TWS API Beta at the time of this writing, all functionality is implemented.
Python is relatively easy-to-use programming language in which you can write code fast. Since it's not statically-typed, there are limitations
to how much IDE can help you with hints, but the advantage is that less code is required.

It'll take much less time to write an equivalent program in Python than in any other language on the list (supposed you know all
the languages equally well). It's quite easy to make trading program and a backtest that use the same trading-logic code, which is what
you want to do if you want to be sure the backtest works correctly. This would take more time in C# or Java.

It runs on Windows, Linux, and Mac.

## The Winner

In most cases, probably 80%+, I'd recommend Python, especially once it comes out of Beta. Smaller and middle-sized trading programs will benefit the most from
the easiness-of-use that comes with Python.

But I would not recommend Python when the project is going to be larger. I'd say that is more than around 10,000 lines of code.
With the increased size the lack of static types can hurt the ability to write robust code.
It's easier to introduce bugs. After a certain project size, it just takes longer to read/write Python code
than when using one of the more strict programming languages.
I'd choose C# when using Windows and Java when using other platforms.

In the end, you want to choose the programming language you know best, or one you want to learn.
If you know all equally well or know none, I'd recommend what I've written above - probably Python, or C#/Java for large projects.
