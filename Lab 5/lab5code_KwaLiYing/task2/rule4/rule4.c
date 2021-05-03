#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>

static unsigned char *ip_address1 = "\x43\xCD\x8E\x4E";
static unsigned char *ip_address2 = "\x9F\xCB\xBC\x5C";
static unsigned char *ip_address3 = "\x9F\xCB\xB8\x33";
static unsigned char *ip_address4 = "\xA2\xF3\xA9\x78";

/* This is the structure we shall use to register our function */
static struct nf_hook_ops nfho;

/* This is the hook function itself */
unsigned int hook_func(void *priv, struct sk_buff *skb,
const struct nf_hook_state *state)
{

  /* This is where you can inspect the packet contained in
  the structure pointed by skb, and decide whether to accept
  or drop it. You can even modify the packet */

  // In this example, we drop all outgoing packets to www.y8.com
  struct iphdr *iph;
  struct tcphdr *tcph;

  iph = (struct iphdr *)skb_network_header(skb);
  tcph = (struct tcphdr *)skb_transport_header(skb);

  if (iph->daddr == *(unsigned int*)(ip_address1) || iph->daddr == *(unsigned int*)(ip_address2) || iph->daddr == *(unsigned int*)(ip_address3) || iph->daddr == *(unsigned int*)(ip_address4)) {
  printk(KERN_INFO "Dropping telnet packet to %d.%d.%d.%d\n",
  ((unsigned char *)&iph->daddr)[0],
  ((unsigned char *)&iph->daddr)[1],
  ((unsigned char *)&iph->daddr)[2],
  ((unsigned char *)&iph->daddr)[3]);
  return NF_DROP;
  } else {
    return NF_ACCEPT;
  }

}

/* Initialization routine */
int init_module()
{ /* Fill in our hook structure */
  nfho.hook = hook_func; /* Handler function */
  nfho.hooknum = NF_INET_LOCAL_OUT; /* First hook for IPv4 */
  nfho.pf = PF_INET;
  nfho.priority = NF_IP_PRI_FIRST; /* Make our function first */
  nf_register_hook(&nfho);
  return 0;
}

/* Cleanup routine */
void cleanup_module()
{
  nf_unregister_hook(&nfho);
}


