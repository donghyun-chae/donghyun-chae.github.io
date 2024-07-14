+++
title = "귀류법 / 간접증명법"
categories = ["Dictionary"]
tags = ["HowToSolveIt"]
weight= 5
+++

# **귀류법 / 간접증명법**

### <span style = 'background-color:#ffdce0'>**귀류법**</span>은 가정으로 부터 명백히 틀린 것을 유도하여 가정이 틀림을 증명하는 것이다.

### <span style = 'background-color:#ffdce0'>**간접증명법**</span>은 정반대의 가정이 거짓임을 보임으로써 어떤 주장이 참임을 증명하는 것이다.

<hr/>

{{< hint normal >}}
**_1._** <span style = 'background-color:#F7DDBE'>**귀류법**</span>

0~9 까지의 숫자를 한 번씩만 사용하여 수를 만드는데 그 수의 합이 100이 되도록 만들어보자.  
구하려는 것은? 100이란 수를 만드는 수의 집합  
조건은? 1. 0-9를 한번씩 사용해야한다. 2. 합이 100이어야 한다.  
조건 가운데 1번만 남겨보면 {19, 28, 37, 46, 50} 은 만족한다.  
2번도 만족하게끔 고민해보면 {19, 28, 30, 7, 6, 5, 4} = 99 이런식으로 추론을 지속한다.  
하지만 몇 번 반복하다보면 이것이 가능한가? 라는 생각이 든다.

이런 의심을 검증해볼 필요가 있다.  
0-9 중 어떤 것은 일의 자리수, 어떤 것은 십의 자리수를 나타낸다.
이것을 수식으로 나타내면 다음과 같다.
![](/img/HowToSolveIt/Dictionary/reductio/1.png)

이를 통해서 t를 결정하는 방정식을 풀어보면 다음과 같다.
![](/img/HowToSolveIt/Dictionary/reductio/2.png)

위 식에서 명백히 잘못된 것을 찾을 수 있는데 t는 정수여야 한다.  
제기된 두 조건을 동시에 만족할 수 있을 것이라는 가정에서 출발했는데 가정이 잘못됐음이 명백히 진 것이다.  
이런 추론으로 가정이 잘못됨을 밝히는 것이 귀류법이다.

<br/>
<br/>

**_2._** **주의**
위 예시에서 모든 조건이 만족되는 상황은 발생할 수 없는 것을 증명했다.  
이러한 상황의 가능성을 예상해야 한다.

<br/>
<br/>

![](/img/HowToSolveIt/Dictionary/induction/3.png)
n = 4 를 <span style = 'background-color:#D6F0FF'>**특수한 상황**</span>이라고 생각하고  
n 을 1부터 넣어보면서 <span style = 'background-color:#D6F0FF'>**지질학자가 어떤 광성 표본을 정리하듯**</span> 정리해 볼 수 있다.

<br/>
<br/>

![](/img/HowToSolveIt/Dictionary/induction/4.png)
일반적인 과학에서 이런 귀납에 의한 증명은 사실로 받아들여지지만 수학의 경우엔 좀 더 엄밀한 증명을 원한다.
<span style = 'background-color:#D6F0FF'>**처음 n개의 수의 세제곱의 합은 어떤 수의 제곱이 된다.**</span> 라는 명제를 증명해야 하는 것이다.
<br/>
<br/>

**_2._** 이런 법칙이 가능한 <span style = 'background-color:#F7DDBE'>**이유**</span>가 무엇일까?  
다른 과학자처럼 n = 1,2,3,4,5 의 경우를 다시 검토해 보자. 어떤 특징이 존재하는가?
![](/img/HowToSolveIt/Dictionary/induction/5.png)

이 수열의 이웃하는 두 항의 차가 증가하는데 명백히 일정하게 증가하고 있다.  
즉 1, 3, 6, 10, 15 에 <span style = 'background-color:#D6F0FF'>**규칙성**</span>이 존재하는 것이다.
![](/img/HowToSolveIt/Dictionary/induction/6.png)

이런 규칙성을 <span style = 'background-color:#D6F0FF'>**일반화**</span>하여 좀 더 정확히 기술 할 수 있다.
![](/img/HowToSolveIt/Dictionary/induction/7.png)

<br/>
<br/>

**_3._** 방금 법칙은 <span style = 'background-color:#F7DDBE'>**귀납**</span>에 의해 발견됐다.  
귀납은 관찰된 사실 뒤의 <span style = 'background-color:#D6F0FF'>**규칙성과 일관성**</span>을 찾는 것이다.  
이때의 가장 중요한 도구는 <span style = 'background-color:#D6F0FF'>**일반화, 특수화, 유추**</span>이다.  
관찰된 사실을 이해하려 노력하고 유추에 근거하며 특수한 경우를 테스트 한다.  
수학은 체계적인 연역의 학문이지만 많은 수학적 발견은 귀납에 의해 이뤄졌다.

<br/>
<br/>

**_4._** 이것을 엄밀히 <span style = 'background-color:#F7DDBE'>**증명**</span>해보자.  
우리는 다음과 같은 사실을 알고 있다.  
![](/img/HowToSolveIt/Dictionary/induction/8.png)

이것은 등차수열이나 기하적 접근으로 쉽게 증명할 수 있다.  
이 식을 통해 증명해야할 문제를 <span style = 'background-color:#D6F0FF'>**변형**</span>할 수 있다.
![](/img/HowToSolveIt/Dictionary/induction/9.png)

<br/>
<br/>

**_5._** 한번에 증명하는 법이 생각나지 않으면 <span style = 'background-color:#F7DDBE'>**테스트**</span>해보자.  
n = 6의 경우를 테스트 하면 다음과 같이 된다.
![](/img/HowToSolveIt/Dictionary/induction/10.png)

양변 모두 441로 성립한다. 모든 n에 대해 참인듯 한데 n+1에 대해서도 참일까?
위의 공식에 n+1을 대입하면 다음과 같다.
![](/img/HowToSolveIt/Dictionary/induction/11.png)

위 식에서 아래 식을 뺌으로써 다른 식을 얻을 수 있다.
![](/img/HowToSolveIt/Dictionary/induction/12.png)

우변을 정리해 보면 다음과 같다.
![](/img/HowToSolveIt/Dictionary/induction/13.png)

즉 양변이 같아지면서 n이 참이면 n+1도 참이여야하고 이는 모든 수(정수)에대해 참임을 의미한다.

<br/>
<br/>

**_6._** 이런 증명은 <span style = 'background-color:#F7DDBE'>**정수에 관한**</span>것임을 명백히 해야한다.  
<span style = 'background-color:#D6F0FF'>**"n 으로부터 n+1"**</span>의 증명은 <span style = 'background-color:#D6F0FF'>**"다음 정수로의 이동"**</span> 이라고도 할 수 있는데 전문적 용어는 <span style = 'background-color:#D6F0FF'>**"수학적 귀납법"**</span>이다.  
이 접근 방식은 귀납에 대한 수학적 보충이라고 볼 수 있다.

<br/>
<br/>

**_7._** 증명의 과정에서 주장은 <span style = 'background-color:#F7DDBE'>**점점 명쾌해져 갔다.**</span>  
처음의 주장은 덜 명확하고 덜 구체적이였고 점점 명확하고 구체적인 주장으로 이행됐다.  
이런 <span style = 'background-color:#D6F0FF'>**명쾌한 주장이 더 정복하기 쉬운 것**</span>이고 이를 발명가의 역설이라 한다.
{{< /hint >}}
