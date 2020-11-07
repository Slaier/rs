# VLAN

一个VLAN就是一个广播域，VLAN之间的通信是通过三层路由来完成的。

为什么要有vlan: 隔离广播域, 应对广播风暴；在二层对数据进行隔离、转发。

---

## VLAN Tag
![Vlan Tag](vlan/vlan.png)

* 802.1q Tag各字段含义

  * TPID：长度为2字节，表示帧类型。取值为0x8100时表示802.1q Tag帧。
  * PRI：Priority，长度为3比特，表示帧的优先级，取值范围为0～7，值越大优先级越高。一般情况下，当交换机部署QoS时，优先发送优先级高的数据帧。
  * CFI：Canonical Format Indicator，长度为1比特，表示MAC地址是否是经典格式。CFI为0说明是经典格式，CFI为1表示为非经典格式。用于区分以太网帧、FDDI（Fiber Distributed Digital Interface）帧和令牌环网帧。在以太网中，CFI的值为0。
  * VID：VLAN ID，长度为12比特，表示该帧所属的VLAN。

---

## PVID/NativeVlan

*   PVID 表示端口在缺省情况下所属的 VLAN。
*   PVID 默认为1。

---

## VLAN 分配

- 基于流 (高优先级)
  acl匹配特定流量，进行vlan分配
- vlan翻译
- 基于smac
- 基于sip掩码
- 基于协议
  - FrameType
    EthernetII, IEEE 802.3 SNAP, IEEE 802.3 LLC
  - EtherType
    IPV4, IPX-RAW, IPX-LLC等
- 基于端口 (低优先级, 默认)

---

## VLAN 端口类型

端口类型用于识别 VLAN 帧，每种端口类型均可配置一个缺省 VLAN。

### Access 端口

Access 端口是交换机上用来连接用户主机的端口，只允许 PVID 通过本端口，出端口方向将vlan tag剥离。

### Trunk 端口

Trunk 端口是交换机上用来和其他交换机连接的端口。Trunk 端口允许多个 VLAN 的帧通过。出端口方向将vlan id 为 pvid 的帧的 vlan tag 剥离。

### Hybrid 端口

Hybrid 端口是交换机上既可以连接用户主机，又可以连接其他交换机的端口。Hybrid 端口允许多个 VLAN 的帧通过，并可以在出端口方向将某些 VLAN 帧的 Tag 剥掉。

---

## QINQ

因为IEEE802.1Q中定义的VLAN Tag域只有12个比特，仅能表示4096个VLAN，无法满足以太网中标识大量用户的需求，于是QinQ技术应运而生。

QinQ（802.1Q-in-802.1Q）通过在802.1Q标签报文的基础上再增加一层802.1Q的Tag来达到扩展VLAN空间的功能。

内层 VLAN Tag：为用户的私网 VLAN Tag，Customer VLAN Tag (简称 CVLAN)。设备依靠该 Tag 在私网中传送报文。

外层 VLAN Tag：为运营商分配给用户的公网 VLAN Tag， Service VLAN Tag(简称 SVLAN)。设备依靠该 Tag 在公网中传送 QinQ 报文。

## Private Vlan

![PVLAN TOPO](vlan/pvlan-topo.png)

为什么要有PVLAN: 隔离hosts, 通常需要给每个隔离host分配不同vlan和ip子网, 浪费资源。

Pvlan 可以将一个 vlan 的二层广播域划分成多个子域, 子域由一对 vlan 组成即主 vlan 和次要vlan 组成。

单个PVLAN 中只有一个主 vlan ,每个子域有不同的次要 vlan, 实现二层网络的隔离。主vlan与次要vlann能相互通信。

次要 vlan 包括隔离 vlan 和团体 vlan。

单个PVLAN中只有一个隔离VLAN，隔离 vlan中的端口互相不能进行二层通信,也不能与其他团体vlan通信。

单个PVLAN中可以有多个团体vlan, 单个团体 vlan 内的端口可以进行二层交换，但不能与其他团体vlan二层通信。

参考文章：
- https://happymiki.github.io/2018/08/07/VLAN/
- https://www.certprepare.com/private-vlan