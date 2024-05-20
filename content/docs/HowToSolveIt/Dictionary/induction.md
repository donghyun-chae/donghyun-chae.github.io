+++
title = "귀납 / 수학적 귀납법"
categories = ["Dictionary"]
tags = ["HowToSolveIt"]
weight= 4
+++

# **귀납 / 수학적 귀납법**

### <span style = 'background-color:#ffdce0'>**귀납**</span>은 특수한 상황에서 일반적인 것을 발견하는 과정이다.

### <span style = 'background-color:#ffdce0'>**수학적 귀납**</span>은 어떤 종류의 정리를 증명하기 위한 것으로 수학에서만 쓰인다.

<hr/>

{{< hint normal >}}
**_1._** <span style = 'background-color:#F7DDBE'>**우연히**</span> 다음 사실을 접했다.
![](/img/HowToSolveIt/Dictionary/induction/1.png)
이런 식에서 각 수를 어떤 수의 **제곱이나 세제곱**으로 바라보면 다음과 같이 다시 바라볼 수 있다.

<br/>
<br/>

![](/img/HowToSolveIt/Dictionary/induction/2.png)

여기서 <span style = 'background-color:#D6F0FF'>**1부터 순차적인 수의 세제곱의 합은 어떤 수의 제곱**</span>이 되는 것을 볼 수 있는데  
이것이 <span style = 'background-color:#D6F0FF'>**일반적으로 적용되는 지**</span>를 연구하는 것이 귀납인 것이다. <span style = 'background-color:#D6F0FF'>**특수한 상황 -> 일반적인 상황**</span>

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
