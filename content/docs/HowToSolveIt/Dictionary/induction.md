+++
title = "귀납 / 수학적 귀납법"
categories = ["Dictionary"]
tags = ["HowToSolveIt"]
weight= 1
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

**_2._** 현명한 사람들은 그런 시도에 너무 많은 시간을 쏟지 않고 <span style = 'background-color:#F7DDBE'>**방향을 바꾸어 거꾸로 생각해본다.**</span>  
구하려는 것이 무엇인가? 우리가 구하려는 상황을 명확히 마음에 그려보자.  
_*"파푸스"는 이미 찾은 것 처럼 가정하라고 한다.*_
![](/img/HowToSolveIt/Dictionary/workingbackwards/2.png)

구하려는 것을 주어진 것으로 얻을 수 있을까?  
_*"파푸스"는 원하는 결과를 어떤 전제에서 구할 수 있는지 물어보라 한다.*_

<span style = 'background-color:#F7DDBE'>큰 용기를 9L 까지 채우고 **그 다음 3L만 쏟아내야 한다**.</span>  
그렇게 하려면 **작은 용기에 1L만 있어야 한다.** <span style = 'background-color:#D6F0FF'>**이 생각이 아이디어다.**</span>

![](/img/HowToSolveIt/Dictionary/workingbackwards/3.png)

이 과정을 **주저 없이 진행하는 사람**은 없을 것이다. 이 단계에 도달하면 해답이 얼추 보일 것이다.

<span style = 'background-color:#D6F0FF'>꼭 이 형태와 흐름으로 생각이 진행되지 않더라도 **같은 상황**에 도달할 수 있다.</span>

![](/img/HowToSolveIt/Dictionary/workingbackwards/4.png)
![](/img/HowToSolveIt/Dictionary/workingbackwards/5.png)

3개의 실마리 중 하나를 떠올리면 **나머지도** 떠올릴 수 있다.  
위 같이 실마리가 되는 생각을 떠올리는 것은 **쉬운 일이 아니다**.

<span style = 'background-color:#F7DDBE'>9L 용기를 가득 채운 후 4L에 따라 2번 버린다. </span>  
_*우리는 마침내 우리가 알고 있는 것에 도달했다 - "파푸스" .*_  
**거꾸로 생각하기 방법의 작동 순서를 살짝 맛봤다.**
![](/img/HowToSolveIt/Dictionary/workingbackwards/6.png)

<span style = 'background-color:#D6F0FF'>**거꾸로 적절한 단계**를 진행하며 우리가 구하려는 것을 구할 수 있게 된다.</span>
<br/>
<br/>

**_3._** 사고과정에 대한 분석은 피상적인 방법 외에 <span style = 'background-color:#ffdce0'>**확실한 어떤 것이 내포되어 있다.**</span>  
거꾸로 생각하는 것은 원하는 목표에 이르는 **가까운 길을 택하지 않고** <span style = 'background-color:#D6F0FF'>**멀어져가기 때문에 심리적 어려움이 있다.**</span>

아주 유능한 사람이라도 주의 깊게 생각하지 않으면 **거꾸로 생각하기는 어렵고 이해하지 못한다.**  
그러나 거꾸로 생각하며 문제를 푸는 것은 어떤 재능도 필요없고 **약간의 상식만**으로 가능하다.  
<span style = 'background-color:#ffdce0'>**원하는 목표에 주의를 집중하고 도달하고 싶은 것의 마지막을 마음속에 그린다.**</span>  
<span style = 'background-color:#ffdce0'>**그곳으로 갈 수 있는 이전 위치는 어디인가? 이렇게 물어보며 거꾸로 생각해 나아가는 것이다.**</span>  
작은 문제도 자연스럽게 거꾸로 생각하기를 실천할 수 있다.
_*"파푸스" 4번 참고*_
<br/>
<br/>

**_4._** 동물과 관련된 심리학적 실험을 살펴보자 <span style = 'background-color:#F7DDBE'>**D에 개를, F에 음식을 놓았다.**</span>  
![](/img/HowToSolveIt/Dictionary/workingbackwards/7.png)

처음에 개는 **바로 음식에 달려들듯 하지만 곧 울타리를 따라 달리며** 음식에 도달하게 된다.  
그러나 <span style = 'background-color:#D6F0FF'>**D와 F가 가까이 놓일 수록**</span> 개는 원할히 도착하기 힘들어진다.  
개는 돌아간다는 아이디어를 떠올리기 전에 담장에 짖고 덤비며 시간을 보낼 것이다.

침팬지에게는 매우 쉬운 문제이고 개는 조금 어려워할테지만 닭은 상당히 오랜 시간이 걸릴 것이다.  
닭도 이리뛰고 저리뛰다 **우연히** 성공할 수는 있을 것이다.

**_4._** 간단한 실험으로 어떤 큰 이론처럼 생각하면 안되지만 **분명히 의미가 있는 실험**이다.
얼렁뚱땅 시도하다 운좋게 성공해도 <span style = 'background-color:#D6F0FF'>**성공하게 된 이유를 이해하지 못하면**</span> 그 사람은 닭같이 행동한 것이다.  
개는 몇번의 시도에 울타리를 돌아갈 것이고 이런 전환은 뛰어난 통찰을 했다는 인상을 준다.  
원하는 것으로 곧장 가지 않고 방향을 바꾸어 목표로 부터 멀어져 가는 것은 상당히 어려운 일이다.  
<span style = 'background-color:#ffdce0'>**닭이 서툴다고 비난하면 안되며 사실 우리의 어려움과 분명한 공통점이 있다.**</span>
{{< /hint >}}
