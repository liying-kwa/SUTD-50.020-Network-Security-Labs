#include <pcap.h>
#include <stdio.h>

/* This function will be invoked by pcap for each captured packet.
We can process each packet inside the function.
*/
void got_packet(u_char *args, const struct pcap_pkthdr *header, const u_char *packet)
{
  printf("Got a packet\n");
}

int main()
{
  pcap_t *handle;
  char errbuf[PCAP_ERRBUF_SIZE];
  struct bpf_program fp;
  char filter_exp[] = "ic proto icmp and ((src 10.0.2.128 and dst 10.0.2.129) or (src 10.0.2.129 and dst 10.0.2.128))";
  bpf_u_int32 net;

  // Step 1: Open live pcap session on NIC with name eth3
  // Students needs to change "eth3" to the name found on their own machines (using ifconfig).
  handle = pcap_open_live("ens33", BUFSIZ, 1, 1000, errbuf);
  // Step 2: Compile filter_exp into BPF psuedo-code
  pcap_compile(handle, &fp, filter_exp, 0, net);
  pcap_setfilter(handle, &fp);
  // Step 3: Capture packets
  pcap_loop(handle, -1, got_packet, NULL);
  pcap_close(handle); //Close the handle
  return 0;
}
